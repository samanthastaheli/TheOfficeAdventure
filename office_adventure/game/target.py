from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class Target(Actor):
    def __init__(self):
        super().__init__()
        self._player = self.set_position(Point(0,0))

    def create_target(self, x, y):
        self._target = self.set_position(Point(x, y))
        self.set_image(constants.IMAGE_DEFAULT)
        self.set_height(constants.TARGET_HEIGHT)
        self.set_width(constants.TARGET_WIDTH)