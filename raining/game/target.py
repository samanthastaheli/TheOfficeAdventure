from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class Target(Actor):
    def __init__(self):
        super().__init__()
        self._target = self.set_position(Point(0,0))
        self._placeholder = self.set_position(Point(0,0))
        self._type = ['dog', 'dog2', 'cat', 'cat2', 'drop', 'umbrella']

    def create_target(self, x, y, type):
        self._target = self.set_position(Point(x, y))
        self.set_height(constants.TARGET_SIZE)
        self.set_width(constants.TARGET_SIZE)
        if type == 'dog':
            self.set_image(constants.IMAGE_DOG)
        elif type == 'dog2':
            self.set_image(constants.IMAGE_DOG2)
        elif type == 'cat':
            self.set_image(constants.IMAGE_CAT)
        elif type == 'cat2':
            self.set_image(constants.IMAGE_CAT2)
        elif type == 'drop':
            self.set_image(constants.IMAGE_DROP)
        elif type == 'umbrella':
            self.set_image(constants.IMAGE_UMBRELLA)
            
    def get_target_type(self):
        return self._type