from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class Obstacle(Actor):
    def __init__(self):
        super().__init__()
        self._obstacle = self.set_position(Point(20,100))

    def create_desk(self, x, y, type):
        self._obstacle = self.set_position(Point(x, y))
        if type == "ver":
            self.set_image(constants.IMAGE_DESK_VER)
            self.set_height(constants.DESK_LONG)
            self.set_width(constants.DESK_SHORT)
        elif type == "hor":
            self.set_image(constants.IMAGE_DESK_HOR)
            self.set_height(constants.DESK_SHORT)
            self.set_width(constants.DESK_LONG)
        elif type == "flat_hor":
            self.set_image(constants.IMAGE_DESK_FLAT_HOR)
            self.set_height(constants.DESK_SHORT)
            self.set_width(constants.DESK_LONG)
        elif type == "flat_ver":
            self.set_image(constants.IMAGE_DESK_FLAT_VER)
            self.set_height(constants.DESK_LONG)
            self.set_width(constants.DESK_SHORT)
        else:
            self.set_height(constants.DESK_LONG)
            self.set_width(constants.DESK_SHORT)
        
    # def create_desk_flat_hor(self, x, y):
    #     self._desk = self.set_position(Point(x, y))
    #     # self.set_image(constants.IMAGE_DESK_FLAT_HOR)
    #     self.set_height(constants.DESK_HEIGHT)
    #     self.set_width(constants.DESK_WIDTH)

    # def create_desk_flat_ver(self, x, y):
    #     self._desk = self.set_position(Point(x, y))
    #     # self.set_image(constants.IMAGE_DESK_FLAT)
    #     self.set_height(constants.DESK_WIDTH)
    #     self.set_width(constants.DESK_HEIGHT)
