from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class Player(Actor):
    def __init__(self):
        super().__init__()
        self._player = self.set_position(Point(0,0))

    def create_player(self, x, y):
        self._player = self.set_position(Point(x, y))
        self.set_image(constants.IMAGE_player)
        self.set_height(constants.PLAYER_HEIGHT)
        self.set_width(constants.PLAYER_WIDTH)