from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class PlaceHolder(Actor):
    def __init__(self):
        super().__init__()
        self._placeholder = self.set_position(Point(0,0))

    def create_placeholder(self, x, y):
        self._placeholder = self.set_position(Point(x, y))
        self.set_image(constants.IMAGE_SQ)
        self.set_height(constants.TARGET_SIZE)
        self.set_width(constants.TARGET_SIZE)