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
        self._type = ['phone', 'plant', 'file', 'dundie', 'tea']

    def create_target(self, x, y, type):
        self._target = self.set_position(Point(x, y))
        if type == 'phone':
            self.set_image(constants.IMAGE_PHONE)
            self.set_height(constants.TARGET_SIZE)
            self.set_width(constants.TARGET_SIZE)
        elif type == 'plant':
            self.set_image(constants.IMAGE_PLANT)
            self.set_height(constants.TARGET_SIZE)
            self.set_width(constants.TARGET_SIZE)
        elif type == 'file':
            self.set_image(constants.IMAGE_FILE)
            self.set_height(constants.TARGET_SIZE)
            self.set_width(constants.TARGET_SIZE)
        elif type == 'dundie':
            self.set_image(constants.IMAGE_DUNDIE)
            self.set_height(constants.TARGET_SIZE)
            self.set_width(constants.TARGET_SIZE)
        elif type == 'tea':
            self.set_image(constants.IMAGE_TEA)
            self.set_height(constants.TARGET_SIZE)
            self.set_width(constants.TARGET_SIZE)

    def create_placeholder(self, x, y):
        self._placeholder = self.set_position(Point(x, y))
        self.set_image(constants.IMAGE_SQ)
        self.set_height(constants.TARGET_SIZE)
        self.set_width(constants.TARGET_SIZE)

    def get_target_type(self):
        return self._type