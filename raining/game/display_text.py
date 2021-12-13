from game.actor import Actor
from game import constants
from game.point import Point
from random import randint
import os

class DisplayText(Actor):
    def __init__(self):
        super().__init__()
        self._text = self.set_text('Default Text')

    def create_text(self, text, x, y):
        self._text = self.set_text(text)
        self.set_position(Point(x, y))
        # self.set_height(constants.TARGET_HEIGHT)
        # self.set_width(constants.TARGET_WIDTH)
    def display_text(self, text, x, y):
        self.create_text(text, x, y)