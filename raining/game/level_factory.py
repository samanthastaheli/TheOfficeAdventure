from game import constants
from game.player import Player
from game.wall import Wall
from game.target import Target
from game.placeholder import PlaceHolder
from game.obstacle import Obstacle
import random
from game.point import Point
from game.actor import Actor

class LevelFactory():
    def __init__(self) -> None:
        self._wall_list = []
        self._obstacle_list = []
        self._target_list = []
        self._player_list = []
        self._placeholder_list = []

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
        # create menu left border
        for y in range(0, constants.MAX_Y, constants.WALL_SIZE):
            wall = Wall()
            wall.create_wall(constants.START_RIGHT, y)
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
        # create inside walls
        # create darryl office right wall
        for y in range(0, int(constants.DESK_SHORT*3), constants.WALL_SIZE_SM):
            wall = Wall()
            wall.create_small_wall(int(constants.WALL_SIZE+constants.DESK_LONG*2), y)
            self._wall_list.append(wall)
        # darryl office bottom wall
        for x in range(int(constants.WALL_SIZE+constants.DOOR_WIDTH), int(constants.WALL_SIZE+constants.DESK_LONG*2), constants.WALL_SIZE_SM):
            wall = Wall()
            wall.create_small_wall(x, y)
            self._wall_list.append(wall)
        
        # michael office left wall / conference right wall
        for y in range(int(constants.MAX_Y-constants.MICHEAL_OFFICE_HEIGHT), constants.MAX_Y, constants.WALL_SIZE_SM):
            wall = Wall()
            wall.create_small_wall(constants.CONF_WIDTH, y)
            self._wall_list.append(wall)
        # michael office right wall
        for y in range(int(constants.MAX_Y-constants.MICHEAL_OFFICE_HEIGHT), constants.MAX_Y, constants.WALL_SIZE_SM):
            wall = Wall()
            wall.create_small_wall(constants.START_LEFT, y)
            self._wall_list.append(wall)
        # conference room top wall
        for x in range(0, int(constants.CONF_WIDTH-constants.DOOR_WIDTH), constants.WALL_SIZE_SM):
            wall = Wall()
            wall.create_small_wall(x, int(constants.MAX_Y-constants.MICHEAL_OFFICE_HEIGHT))
            self._wall_list.append(wall)
        # michael office top wall
        for x in range(int(constants.CONF_WIDTH+constants.DOOR_WIDTH), constants.MICHEAL_OFFICE_WIDTH, constants.WALL_SIZE_SM):
            wall = Wall()
            wall.create_small_wall(x, int(constants.MAX_Y-constants.MICHEAL_OFFICE_HEIGHT))
            self._wall_list.append(wall)

    def get_walls(self):
        return self._wall_list

    def build_desk(self):
        # top row desks 
        # desks 1
        desk_darryl = Obstacle()
        desk_darryl.create_desk(int(constants.WALL_SIZE + constants.DESK_SHORT), int(constants.WALL_SIZE+constants.DESK_SHORT), "hor")
        self._obstacle_list.append(desk_darryl)

        # desk 3,5
        desk_creed = Obstacle()
        desk_creed.create_desk(int(constants.WALL_SIZE + constants.BORDER*2 + constants.DESK_SHORT*2), constants.WALL_SIZE, "ver")
        self._obstacle_list.append(desk_creed)

        desk_merdith = Obstacle()
        desk_merdith.create_desk(int(constants.WALL_SIZE + constants.BORDER*2 + constants.DESK_SHORT*3), constants.WALL_SIZE, "ver")
        self._obstacle_list.append(desk_merdith)

        # desk 5,6,7
        desk_oscar = Obstacle()
        desk_oscar.create_desk(int(constants.START_RIGHT - constants.DESK_LONG - constants.DESK_SHORT), int(constants.WALL_SIZE + constants.DESK_SHORT), "ver")
        self._obstacle_list.append(desk_oscar)

        desk_kevin = Obstacle()
        desk_kevin.create_desk(int(constants.START_RIGHT - constants.DESK_LONG), int(constants.WALL_SIZE + constants.DESK_SHORT), "flat_hor")
        self._obstacle_list.append(desk_kevin)

        desk_angela = Obstacle()
        desk_angela.create_desk(int(constants.START_RIGHT - constants.DESK_LONG), int(constants.WALL_SIZE + constants.DESK_SHORT*2), "hor")
        self._obstacle_list.append(desk_angela)

        # sec row desks
        # desks 8,9,10
        desk_stanley = Obstacle()
        desk_stanley.create_desk(int(constants.WALL_SIZE + constants.BORDER), int(constants.WALL_SIZE+constants.DESK_LONG+constants.BORDER), "flat_ver")
        self._obstacle_list.append(desk_stanley)

        desk_phylis = Obstacle()
        desk_phylis.create_desk(int(constants.WALL_SIZE + constants.BORDER + constants.DESK_SHORT), int(constants.WALL_SIZE+constants.DESK_LONG+constants.BORDER), "flat_ver")
        self._obstacle_list.append(desk_phylis)

        desk_andy = Obstacle()
        desk_andy.create_desk(int(constants.WALL_SIZE + constants.BORDER), int(constants.WALL_SIZE+constants.DESK_LONG*2+constants.BORDER), "hor")
        self._obstacle_list.append(desk_andy)

        # desks 11,12
        desk_dwight = Obstacle()
        desk_dwight.create_desk(int(constants.WALL_SIZE + constants.BORDER*2 + constants.DESK_SHORT*2), int(constants.WALL_SIZE+constants.DESK_LONG+constants.BORDER), "flat_ver")
        self._obstacle_list.append(desk_dwight)

        desk_jim = Obstacle()
        desk_jim.create_desk(int(constants.WALL_SIZE + constants.BORDER*2 + constants.DESK_SHORT*2), int(constants.WALL_SIZE+constants.DESK_LONG*2+constants.BORDER), "hor")
        self._obstacle_list.append(desk_jim)

        # desk 13 and barrier
        desk_pam = Obstacle()
        desk_pam.create_desk(int(constants.START_RIGHT - constants.DESK_LONG - constants.WALL_SIZE), int(constants.WALL_SIZE+constants.DESK_LONG+constants.BORDER), "ver")
        self._obstacle_list.append(desk_pam)

        # confernece room and michael office desks
        desk_michael = Obstacle()
        desk_michael.create_desk(int(constants.CONF_WIDTH + constants.DESK_SHORT), int(constants.MAX_Y-constants.DESK_SHORT*2), "hor")
        self._obstacle_list.append(desk_michael)

        desk_conf = Obstacle()
        desk_conf.create_desk(int(constants.WALL_SIZE + constants.DESK_LONG), int(constants.MAX_Y-constants.WALL_SIZE-(constants.MICHEAL_OFFICE_HEIGHT/2)), "flat_hor")
        self._obstacle_list.append(desk_conf)

    def get_obstacles(self):
        return self._obstacle_list

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

    def build_placeholders(self):
        place1 = PlaceHolder()
        x = int(constants.MAX_X-constants.WALL_SPACE*3)
        y = int(constants.BORDER)
        place1.create_placeholder(x, y)
        self._placeholder_list.append(place1)

        place2 = PlaceHolder()
        x = int(constants.MAX_X-constants.WALL_SPACE*2)
        y = int(constants.BORDER)
        place2.create_placeholder(x, y)
        self._placeholder_list.append(place2)

        place3 = PlaceHolder()
        x = int(constants.MAX_X-constants.WALL_SPACE)
        y = int(constants.BORDER)
        place3.create_placeholder(x, y)
        self._placeholder_list.append(place3)

        place4 = PlaceHolder()
        x = int(constants.MAX_X-constants.WALL_SPACE*3)
        y = int(constants.BORDER + constants.TARGET_SIZE + constants.WALL_SIZE*2)
        place4.create_placeholder(x, y)
        self._placeholder_list.append(place4)

        place5 = PlaceHolder()
        x = int(constants.MAX_X-constants.WALL_SPACE*2)
        y = int(constants.BORDER + constants.TARGET_SIZE + constants.WALL_SIZE*2)
        place5.create_placeholder(x, y)
        self._placeholder_list.append(place5)

        place6 = PlaceHolder()
        x = int(constants.MAX_X-constants.WALL_SPACE)
        y = int(constants.BORDER + constants.TARGET_SIZE + constants.WALL_SIZE*2)
        place6.create_placeholder(x, y)
        self._placeholder_list.append(place6)
        # # build top row
        # i = 1
        # for i in range(int(constants.TARGET_COUNT/2+1)):
        #     placeholder = PlaceHolder()
        #     x = int(constants.MAX_X-constants.WALL_SPACE*i)
        #     y = int(constants.BORDER)
        #     placeholder.create_placeholder(x, y)
        #     self._target_list.append(placeholder)
        #     i+=1
        # # build bottom row
        # for i in range(int(constants.TARGET_COUNT/2+1)):
        #     placeholder = Target()
        #     x = int(constants.MAX_X-constants.WALL_SPACE*i)
        #     y = int(constants.BORDER + constants.TARGET_SIZE + constants.WALL_SIZE*2)
        #     placeholder.create_placeholder(x, y)
        #     self._target_list.append(placeholder)
        #     i+=1
    
    def get_placeholders(self):
        return self._placeholder_list

    def get_targets(self):
        return self._target_list

    def build_player(self):
        player = Player()
        player.create_player(int(constants.START_LEFT + constants.WALL_SIZE), int(constants.MAX_Y-constants.WALL_SIZE-constants.BORDER))
        self._player_list.append(player)

    def get_player(self):
        return self._player_list