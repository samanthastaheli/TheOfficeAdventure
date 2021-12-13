import os

MAX_X = 1000
MAX_Y = int(MAX_X - MAX_X*0.25)
FRAME_RATE = 30

BORDER = 200

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_DEFAULT = os.path.join(os.getcwd(), "./raining/assets/donatello.png")
IMAGE_DOG = os.path.join(os.getcwd(), "./raining/assets/dog.png")
IMAGE_DOG2 = os.path.join(os.getcwd(), "./raining/assets/australian-shepherd.png")
IMAGE_CAT = os.path.join(os.getcwd(), "./raining/assets/cat.png")
IMAGE_CAT2 = os.path.join(os.getcwd(), "./raining/assets/cat2.png")
IMAGE_DROP = os.path.join(os.getcwd(), "./raining/assets/drop.png")
IMAGE_UMBRELLA = os.path.join(os.getcwd(), "./raining/assets/umbrella.png")


SOUND_START = os.path.join(os.getcwd(), "./office_adventure/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./office_adventure/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./office_adventure/assets/over.wav")
SOUND_AWARD = os.path.join(os.getcwd(), "./office_adventure/assets/award.mp3")

WALL_SIZE = int(MAX_X / 80)
WALL_SIZE_SM = int(WALL_SIZE / 3)
WALL_SPACE = int(MAX_Y / 10)

MAZE_WIDTH = MAX_X - (BORDER*2)
MAZE_HEIGHT = MAX_Y - (BORDER*2)

MENU_WIDTH = int(MAX_X * 0.3)

DESK_LONG = 200
DESK_SHORT = 100

DESK_COUNT = 14

TARGET_X = MAX_X / 2
TARGET_Y = MAX_Y - 25

TARGET_SIZE = 50
TARGET_COUNT = 6
TARGET_SPEED = 2

RANGE_Y = BORDER*3
RANGE_X = MAX_X-WALL_SIZE

PLAYER_SIZE = WALL_SIZE*2

PLAYER_X = MAX_X - MENU_WIDTH - WALL_SPACE - 10
PLAYER_Y = MAX_Y - 125

PLAYER_DX = 8
PLAYER_DY = PLAYER_DX * -1

PLAYER_SPEED = 12

# variables for calculating placement of actors
START_LEFT = int(MAX_X - WALL_SPACE - MENU_WIDTH)
START_RIGHT = int(START_LEFT + WALL_SPACE)
CONF_WIDTH = int(WALL_SPACE+DESK_LONG*3)
CONF_HEIGHT = int(MAX_Y - DESK_SHORT*4)
MICHEAL_OFFICE_WIDTH = START_LEFT
MICHEAL_OFFICE_HEIGHT = int(DESK_SHORT*4)
DOOR_WIDTH = int(WALL_SPACE)