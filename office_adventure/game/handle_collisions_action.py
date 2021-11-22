import random
from game import constants
from game.action import Action
from game.audio_service import AudioService
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. 
    The responsibility of this class of actorects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        self._audio_service = AudioService()

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # get cast
        paddle = cast["paddles"][0]
        bricks = cast["bricks"]
        balls = cast["balls"]

        for ball in balls:
            if self._physics_service.is_collision(ball, paddle):
                self.check_collision(ball, paddle)
            for brick in bricks:
                if self._physics_service.is_collision(ball, brick):
                    self.check_collision(ball, brick)
                    bricks.remove(brick)

    def check_collision(self, actor1, actor2):
        ''' Checks whihc axis collision was. Changes ball direction.
        todo: play sound when collison happens 

        Arg:
            actor1: actor from cast dictionary (usually ball)
            actor2: actor from cast dictionary (usually paddle)
        '''
        if self.check_direction(actor1, actor2) == 'top' or self.check_direction(actor1, actor2) == 'bottom':
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
            self.bounce_y(actor1)
        elif self.check_direction(actor1, actor2) == 'left' or self.check_direction(actor1, actor2) == 'right':
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
            self.bounce_x(actor1)

    def check_direction(self, ball, actor2):
        '''Checks what direction ball needs to go when it collides with brick or paddle.
        Args:
            ball: ball actor
            actor2: another actor, ususally brick or paddle
        '''
        position = ball.get_position()
        x = position.get_x()
        y = position.get_y()

        if ball.get_bottom_edge() >= actor2.get_top_edge():
            ball.set_position(Point(x, (y - constants.BRICK_SPACE)))
            return 'top'
        elif ball.get_top_edge() <= actor2.get_bottom_edge():
            ball.set_position(Point(x, (y + constants.BRICK_SPACE)))
            return 'bottom'
        elif ball.get_left_edge() <= actor2.get_right_edge():
            return 'left'
        elif ball.get_right_edge() >= actor2.get_left_edge():
            return 'right'
        else:
            return 'none'
    
    def bounce_x(self, ball):
        dx = ball.get_velocity().get_x()
        dy = ball.get_velocity().get_y()
        ball.set_velocity(Point(-dx,dy))
        
    def bounce_y(self, ball):
        dx = ball.get_velocity().get_x()
        dy = ball.get_velocity().get_y()
        ball.set_velocity(Point(dx,-dy))