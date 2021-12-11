from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class Wall(Actor):
    def __init__(self):
        super().__init__()
        self._wall = self.set_position(Point(20,100))

    def create_wall(self, x, y):
        self._wall = self.set_position(Point(x, y))
        # self.set_image(constants.IMAGE_DEFAULT)
        self.set_height(constants.WALL_SIZE)
        self.set_width(constants.WALL_SIZE)