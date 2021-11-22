import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class HandleOffScreenAction(Action):
    """A code template for handling when ball goes off screen. 
    The responsibility of this class is so make the ball change directions when gets to off screen points.
    """
    def __init__(self, cast):
        super().__init__()
        self._cast = cast

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]
        
        if self.check_bounce(ball) == 'left':
            self.bounce_x(ball)
            print('bounced left')
        elif self.check_bounce(ball) == 'right':
            self.bounce_x(ball)
            print('bounced right')
        elif self.check_bounce(ball) == 'top':
            self.bounce_y(ball)
            print('bounced top')
        elif self.check_bounce(ball) == 'bottom':
            self.bounce_y(ball)
            print('bounced bottom')

        
    def check_bounce(self, ball):
        """
        Returns value (left,right,top,bottom) if the ball is off screen.
        """
        if ball.get_left_edge() <= 0:
            return 'left'
        elif ball.get_right_edge() >= constants.MAX_X:
            return 'right'
        elif ball.get_top_edge() <= 0:
            return 'top'
        elif ball.get_bottom_edge() >= constants.MAX_Y:
            return 'bottom'

    def bounce_x(self, ball):
        dx = ball.get_velocity().get_x()
        dy = ball.get_velocity().get_y()
        ball.set_velocity(Point(-dx,dy))
        
    def bounce_y(self, ball):
        dx = ball.get_velocity().get_x()
        dy = ball.get_velocity().get_y()
        ball.set_velocity(Point(dx,-dy))