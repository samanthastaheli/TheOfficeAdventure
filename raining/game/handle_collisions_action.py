import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.audio_service import AudioService
from game.point import Point
from game.level_factory import LevelFactory

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
        player = cast["player"][0]
        targets = cast["targets"]
        walls = cast["walls"]

        for wall in walls:
            if self._physics_service.is_collision(player, wall):
                self.check_collision(player, wall)
                # print('Collision!!!!')
        for target in targets:
            if self._physics_service.is_collision(player, target):
                if self.check_direction(player, target) != 'none':
                    self.add_inventory(target)
                    self._audio_service.play_sound(constants.SOUND_AWARD)

    def check_collision(self, actor1, actor2):
        ''' Checks which axis collision was.
            Checks if target collides with player
        Arg:
            actor1: actor from cast dictionary (usually player)
            actor2: actor from cast dictionary (usually wall, obstacle, or target)
        '''

        if self.check_direction(actor1, actor2) == 'top':
            self.stop_top(actor1)
        elif self.check_direction(actor1, actor2) == 'bottom':
            self.stop_bottom(actor1)
        elif self.check_direction(actor1, actor2) == 'left':
            self.stop_left(actor1)
        elif self.check_direction(actor1, actor2) == 'right':
            self.stop_right(actor1)

        '''
        if self.check_direction(actor1, actor2) == 'top' or self.check_direction(actor1, actor2) == 'bottom':
            # self.stop_actor(actor1)
            self.change_y(actor1)
        elif self.check_direction(actor1, actor2) == 'left' or self.check_direction(actor1, actor2) == 'right':
            # self.stop_actor(actor1)
            self.change_x(actor1)

        overlap = self.get_collision_overlap(actor1, actor2)
    
        # if overlap_x >= 0 or overlap_y >= 0:
        #     actor2.set_velocity(0)
        # else:
        #     actor2.set_velocity(constants.PLAYER_SPEED)
        
        if overlap.get_x() <= overlap.get_y():
            # Depth was least along the x-axis, so that's our point of collision
            if overlap.get_x() >= 0:
                #Collision on the left
                actor2.set_position()
            else:
                #Collision on the right
                actor2.set_position()
        else:
        #Collision on the y-axis
            if overlap.get_y() >= 0:
                #Collision on the top
                actor2.set_position()
            else:
                #Collision on the bottom
                actor2.set_position()
        '''
        
    def get_collision_overlap(self, actor1, actor2):
        '''
        Using approach from here: https://stackoverflow.com/a/56607347
        The general idea is: Find the depth the actor1 has gone into the
        actor2, and then the one with the smallest depth is our collision side
        '''
        actor1HalfWidth = actor1.get_width() / 2;
        actor1HalfHeight = actor1.get_height() / 2;
        actor2HalfWidth = actor2.get_width() / 2;
        actor2HalfHeight = actor2.get_height() / 2;
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
            actor2: another actor (wall, obstacle, or target)
        '''
        position = actor1.get_position()
        x = position.get_x()
        y = position.get_y()

        if actor1.get_bottom_edge() >= actor2.get_top_edge():
            # print('Collision Top!')
            return 'top'
        elif actor1.get_top_edge() <= actor2.get_bottom_edge():
            # print('Collision Bottom!')
            return 'bottom'
        elif actor1.get_left_edge() <= actor2.get_right_edge():
            # print('Collision Left!')
            return 'left'
        elif actor1.get_right_edge() >= actor2.get_left_edge():
            # print('Collision Right!')
            return 'right'
        else:
            return 'none'
      
    def stop_actor(self, actor):
        ''' change velocity when needed
        Args: the actor (key in cast dict) to change its velocity
        '''
        dx = actor.get_velocity().get_x()
        dy = actor.get_velocity().get_y()
        actor.set_velocity(Point(dx*0,dy*0))
        print('Stop Actor Called!')

    def change_y(self, actor):
        ''' change velocity when needed
        Args: the actor (key in cast dict) to change its velocity
        '''
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        actor.set_position(Point(x, (y - constants.PLAYER_SIZE)))
        
    def stop_left(self, actor):
        ''' change velocity when needed
        Args: the actor (key in cast dict) to change its velocity
        '''
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        actor.set_position(Point((x - 1), y))
    
    

    def stop_left(self, actor):
        ''' change player position based on collison direction
        Args: the actor (key in cast dict) to change its position 
        '''
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        actor.set_position(Point((x - 1), y))
    
    def stop_right(self, actor):
        ''' change player position based on collison direction
        Args: the actor (key in cast dict) to change its position 
        '''
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        actor.set_position(Point((x - constants.PLAYER_SIZE), y))

    def stop_top(self, actor):
        ''' change player position based on collison direction
        Args: the actor (key in cast dict) to change its position 
        '''
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        actor.set_position(Point(x, (y - 1)))

    def stop_bottom(self, actor):
        ''' change player position based on collison direction
        Args: the actor (key in cast dict) to change its position 
        '''
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        actor.set_position(Point(x, (y - constants.PLAYER_SIZE)))

    def add_inventory(self, target):
        '''changes position of target to offscreen
        Args: target: the target that has collided with player
        '''
        x = int(constants.MAX_X-100)
        y = int(constants.MAX_Y+100)
        target.set_position(Point(x, y))