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
        position = actor1.get_position()
        x = position.get_x()
        y = position.get_y()

        # TODO: add if statement
        if self.check_direction(actor1, actor2) == 'top' or self.check_direction(actor1, actor2) == 'bottom':
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
            actor1.set_position(Point(x, (y - (f'constants.{actor1}_HEIGHT'))))
        elif self.check_direction(actor1, actor2) == 'left' or self.check_direction(actor1, actor2) == 'right':
            self._audio_service.play_sound(constants.SOUND_BOUNCE)
            actor1.set_position(Point((x - (f'constants.{actor1}_WIDTH')), y))

    def get_collision_overlap(actor1, actor2):
        '''
        Using approach from here: https://stackoverflow.com/a/56607347
        The general idea is: Find the depth the actor1 has gone into the
        actor2, and then the one with the smallest depth is our collision side
        '''
        actor1HalfWidth = actor1.GetWidth() / 2;
        actor1HalfHeight = actor1.GetHeight() / 2;
        actor2HalfWidth = actor2.GetWidth() / 2;
        actor2HalfHeight = actor2.GetHeight() / 2;
        # Find the centers
        actor1_center_x = actor1.get_position().get_x() + actor1HalfWidth;
        actor1_center_y = actor1.get_position().get_y() + actor1HalfHeight;
        actor2_center_x = actor2.get_position().get_x() + actor2HalfWidth;
        actor2_center_y = actor2.get_position().get_y() + actor2HalfHeight;
        # Find the distance between centers
        diffx = actor1_center_x - actor2_center_x;
        diffy = actor1_center_y - actor2_center_y;
        # Figure out how close the objects can get without overlapping
        # (When they just barely touch, it's the distance from the center to
        # the edge of the actor1, which is half its width, and then the distance from the
        # edge of the actor2 to its center which is half its width, etc.)
        distanceToOverlapx = actor1HalfWidth + actor2HalfWidth;
        distanceToOverlapy = actor1HalfHeight + actor2HalfHeight;
        # Now find the amount of depth of the overlap
        depthx = distanceToOverlapx - diffx
        depthy = distanceToOverlapy - diffy
        # Now set it to be negative if it overlapped from the right or bottom
        if (diffx > 0):
            depthx *= -1;
        if (diffy > 0):
            depthy *= -1;
        return Point(depthx, depthy)

    def check_direction(self, actor1, actor2):
        '''Checks what direction ball needs to go when it collides with brick or player.
        Args:
            actor1: an actor (player)
            actor2: another actor (wall or obstacle)
        '''
        position = actor1.get_position()
        x = position.get_x()
        y = position.get_y()

        if actor1.get_bottom_edge() >= actor2.get_top_edge():
            return 'top'
        elif actor1.get_top_edge() <= actor2.get_bottom_edge():
            return 'bottom'
        elif actor1.get_left_edge() <= actor2.get_right_edge():
            return 'left'
        elif actor1.get_right_edge() >= actor2.get_left_edge():
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