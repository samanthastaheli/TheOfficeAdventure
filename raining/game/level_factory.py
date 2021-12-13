from game import constants
from game.player import Player
from game.wall import Wall
from game.target import Target
import random
from game.point import Point
from game.actor import Actor

class LevelFactory():
    def __init__(self) -> None:
        self._wall_list = []
        self._target_list = []
        self._player_list = []

    def build_walls(self):        
        # create top of maze
        for x in range(0, int(constants.WALL_SIZE + constants.MAX_X), constants.WALL_SIZE):
            wall = Wall()
            wall.create_wall(x, 0)
            self._wall_list.append(wall)
            x+=constants.WALL_SIZE
        # create bottom border
        for x in range(0, constants.MAX_X, constants.WALL_SIZE):
            wall = Wall()
            wall.create_wall(x, int(constants.MAX_Y-constants.WALL_SIZE))
            self._wall_list.append(wall)
        # create right border
        for y in range(0, constants.MAX_Y, constants.WALL_SIZE):
            wall = Wall()
            wall.create_wall(int(constants.MAX_X-constants.WALL_SIZE), y)
            self._wall_list.append(wall)
        # create left border
        for y in range(0, constants.MAX_Y, constants.WALL_SIZE):
            wall = Wall()
            wall.create_wall(0, y)
            self._wall_list.append(wall)

    def get_walls(self):
        return self._wall_list

    def build_targets(self):
        # target = Target()
        # target.create_target(100, 100, 'phone')
        # self._target_list.append(target)

        # plant1 = Target()
        # plant1.create_target(int(constants.START_LEFT+constants.WALL_SIZE), int(constants.MAX_Y-constants.BORDER*2), 'plant')
        # self._target_list.append(plant1)

        for _ in range(constants.TARGET_COUNT):
            x = random.randint(constants.WALL_SPACE, constants.RANGE_X)
            y = random.randint(constants.WALL_SPACE, constants.RANGE_Y)
            target = Target()
            type = random.choice(target.get_target_type())
            target.create_target(x, y, type)
            self._target_list.append(target)

    def get_targets(self):
        return self._target_list

    def build_player(self):
        player = Player()
        player.create_player(int(constants.START_LEFT + constants.WALL_SIZE), int(constants.MAX_Y-constants.WALL_SIZE-constants.BORDER))
        self._player_list.append(player)

    def get_player(self):
        return self._player_list