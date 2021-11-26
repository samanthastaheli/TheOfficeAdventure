import os

MAX_X = 1200
MAX_Y = 800
FRAME_RATE = 30

BORDER = 10

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_DEFAULT = os.path.join(os.getcwd(), "./batter/assets/pam.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

PLAYER_X = MAX_X / 2
PLAYER_Y = MAX_Y - 125

PLAYER_DX = 8
PLAYER_DY = PLAYER_DX * -1

TARGET_X = MAX_X / 2
TARGET_Y = MAX_Y - 25

TARGET_SPEED = 15

TARGET_WIDTH = 100
TARGET_HEIGHT = 50

PLAYER_WIDTH = 100
PLAYER_HEIGHT = 100

