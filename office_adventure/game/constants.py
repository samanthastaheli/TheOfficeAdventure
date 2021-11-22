import os

MAX_X = 1200
MAX_Y = 800
FRAME_RATE = 30

BORDER = 10

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

# IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/brick-3.png")
IMAGE_BRICK = os.path.join(os.getcwd(), "./batter/assets/lego_brick.png")
# IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/bat.png")
IMAGE_PADDLE = os.path.join(os.getcwd(), "./batter/assets/ping_pong_paddle.png")
# IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ball.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./batter/assets/ping_pong_ball.png")

SOUND_START = os.path.join(os.getcwd(), "./batter/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./batter/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./batter/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

PADDLE_X = MAX_X / 2
PADDLE_Y = MAX_Y - 25

BRICK_WIDTH = 100
BRICK_HEIGHT = 35

BRICK_SPACE = 10

BRICK_ROWS = 5
BRICK_COLUMNS = 12

PADDLE_SPEED = 15

PADDLE_WIDTH = 100
PADDLE_HEIGHT = 50

BALL_WIDTH = 100
BALL_HEIGHT = 100

