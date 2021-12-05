import os

MAX_X = 2000
MAX_Y = 1500
FRAME_RATE = 30

BORDER = 200

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_DEFAULT = os.path.join(os.getcwd(), "./office_adventure/assets/donatello.png")
IMAGE_TARGET = os.path.join(os.getcwd(), "./office_adventure/assets/red_block.png")


SOUND_START = os.path.join(os.getcwd(), "./office_adventure/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./office_adventure/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./office_adventure/assets/over.wav")

PLAYER_X = MAX_X / 2
PLAYER_Y = MAX_Y - 125

PLAYER_DX = 8
PLAYER_DY = PLAYER_DX * -1

PLAYER_SPEED = 10

TARGET_X = MAX_X / 2
TARGET_Y = MAX_Y - 25

# TARGET_SPEED = 0

TARGET_WIDTH = 100
TARGET_HEIGHT = 100

BLOCK_COUNT = 12
RANGE_Y = 1200
RANGE_X = MAX_X

PLAYER_WIDTH = 75
PLAYER_HEIGHT = 75

WALL_WIDTH = 100
WALL_HEIGHT = 100
WALL_SPACE = 100

WALL_X = 100
WALL_Y = 100

MAZE_WIDTH = MAX_X - (BORDER*2)
MAZE_HEIGHT = MAX_Y - (BORDER*2)
