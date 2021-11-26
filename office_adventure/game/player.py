from game import constants
from game.actor import Actor
from game.point import Point

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._player = self.set_position(Point(0,0))

    def create_player(self):
        self._player = self.set_position(Point(int(constants.PLAYER_X), int(constants.PLAYER_Y)))
        self.set_image(constants.IMAGE_DEFAULT)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_width(constants.PLAYER_WIDTH)