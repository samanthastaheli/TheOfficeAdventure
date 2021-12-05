from game import constants
from game.player import Player
from game.wall import Wall
from game.target import Target
from random import randint
from game.point import Point
from game.actor import Actor

class LevelFactory():
    def __init__(self) -> None:
        self._wall = Wall()

    def create_maze(self):
        self._wall.create_wall(constants.WALL_X, constants.WALL_Y)