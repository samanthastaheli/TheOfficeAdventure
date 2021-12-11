import os

MAX_X = 2000
MAX_Y = MAX_X - 500
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

TARGET_X = MAX_X / 2
TARGET_Y = MAX_Y - 25

# TARGET_SPEED = 0

TARGET_WIDTH = 100
TARGET_HEIGHT = 100

BLOCK_COUNT = 12
RANGE_Y = 1200
RANGE_X = MAX_X

WALL_SIZE = int(MAX_X / 80)
WALL_SPACE = int(MAX_Y / 10)

MAZE_WIDTH = MAX_X - (BORDER*2)
MAZE_HEIGHT = MAX_Y - (BORDER*2)

MENU_WIDTH = 500

PLAYER_WIDTH = 75
PLAYER_HEIGHT = 75

PLAYER_X = MAX_X - MENU_WIDTH - WALL_SPACE - 10
PLAYER_Y = MAX_Y - 125

PLAYER_DX = 8
PLAYER_DY = PLAYER_DX * -1

PLAYER_SPEED = 10