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
        # player = cast["players"][0]
        # target = cast["target"]

    def check_collision(self, actor1, actor2):
        ''' Checks which axis collision was.
            Checks if target collides with player
        Arg:
            actor1: actor from cast dictionary (usually target)
            actor2: actor from cast dictionary (usually player)
        '''
        # TODO: add if statement
        pass

    def check_direction(self, target, actor2):
        '''Checks what direction ball needs to go when it collides with brick or player.
        Args:
            target: target (object to be found) actor
            actor2: another actor, ususally brick or player
        '''
        position = target.get_position()
        x = position.get_x()
        y = position.get_y()

        if target.get_bottom_edge() >= actor2.get_top_edge():
            target.set_position(Point(x, (y - constants.BORDER)))
            return 'top'
        elif target.get_top_edge() <= actor2.get_bottom_edge():
            target.set_position(Point(x, (y + constants.BORDER)))
            return 'bottom'
        elif target.get_left_edge() <= actor2.get_right_edge():
            return 'left'
        elif target.get_right_edge() >= actor2.get_left_edge():
            return 'right'
        else:
            return 'none'
    
    def bounce_x(self, target):
        dx = target.get_velocity().get_x()
        dy = target.get_velocity().get_y()
        target.set_velocity(Point(-dx,dy))
        
    def bounce_y(self, target):
        dx = target.get_velocity().get_x()
        dy = target.get_velocity().get_y()
        target.set_velocity(Point(dx,-dy))