# import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.paddle import Paddle
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_offscreen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    # create all actors for the cast to be added to later
    cast["bricks"] = []
    cast["balls"] = []
    cast["paddle"] = []

    # TODO: Create bricks here and add them to the list
    brick_list = []

    for y in range(constants.BORDER, (constants.BRICK_SPACE + constants.BRICK_HEIGHT) * constants.BRICK_ROWS, constants.BRICK_SPACE + constants.BRICK_HEIGHT):
        for x in range(constants.BORDER, (constants.BRICK_SPACE + constants.BRICK_WIDTH) * constants.BRICK_COLUMNS, constants.BRICK_SPACE + constants.BRICK_WIDTH):
            brick = Brick()
            brick.create_brick(x,y)
            brick_list.append(brick)
    cast["bricks"] = brick_list

    # TODO: Create a ball here and add it to the list
    ball_list = []
    ball = Ball()
    ball.create_ball(int(constants.BALL_X), int(constants.BALL_Y))
    ball_list.append(ball)
    cast["balls"] = ball_list

    # TODO: Create a paddle here and add it to the list
    paddle_list = []
    paddle = Paddle()
    paddle.create_paddle()
    paddle_list.append(paddle)
    cast["paddles"] = paddle_list

    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    # TODO: Create additional actions here and add them to the script
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_offscreen_action = HandleOffScreenAction(cast)
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_offscreen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]



    # Start the game
    output_service.open_window("Batter");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
