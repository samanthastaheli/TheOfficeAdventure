from game import constants
from game.actor import Actor
from game.point import Point

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._player = self.set_position(Point(0,0))

    def create_player(self, x, y):
        self._player = self.set_position(Point(x, y))
        self.set_image(constants.IMAGE_DEFAULT)
        self.set_height(int(24))
        self.set_width(int(24))
        # self.set_velocity(Point(constants.PLAYER_SPEED, constants.PLAYER_SPEED))