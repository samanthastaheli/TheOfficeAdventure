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
from game.player import Player
from game.level_factory import LevelFactory
from game.wall import Wall
from game.target import Target
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_offscreen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction
import random

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    cast["player"] = []
    cast["targets"] = []
    cast["walls"] = []
    cast["levels"] = []

    # CREATE PLAYER
    player_list = []
    player = Player()
    player.create_player()
    player_list.append(player)
    cast["player"] = player_list

    # CREATE WALLS
    wall_list = []
    # create top of maze
    for x in range(0, int(constants.WALL_SIZE + constants.MAX_X), constants.WALL_SIZE):
        wall = Wall()
        wall.create_wall(x, 0)
        wall_list.append(wall)
        x+=constants.WALL_SIZE
    # create bottom left border
    left_end = int(constants.MAX_X - constants.WALL_SPACE - constants.MENU_WIDTH)
    for x in range(0, left_end, constants.WALL_SIZE):
        wall = Wall()
        wall.create_wall(x, constants.MAX_Y-constants.BORDER)
        wall_list.append(wall)
    # create bottom menu bottom border
    right_start = int(left_end + constants.WALL_SPACE)
    for x in range(right_start, constants.MAX_X, constants.WALL_SIZE): 
        wall = Wall()
        wall.create_wall(x, int(constants.MAX_Y-constants.WALL_SIZE))
        wall_list.append(wall)
    # create menu left border
    for y in range(0, constants.MAX_Y, constants.WALL_SIZE):
        wall = Wall()
        wall.create_wall(right_start, y)
        wall_list.append(wall)
    # create right border
    for y in range(0, constants.MAX_Y, constants.WALL_SIZE):
        wall = Wall()
        wall.create_wall(int(constants.MAX_X-constants.WALL_SIZE), y)
        wall_list.append(wall)
    # create left border
    for y in range(0, constants.MAX_Y, constants.WALL_SIZE):
        wall = Wall()
        wall.create_wall(0, y)
        wall_list.append(wall)
    # create obstacles 
    # create obstacles type 1
    # for _ in range(constants.BLOCK_COUNT): 
    #     x = random.randint(0, constants.RANGE_X)
    #     y = random.randint(0, constants.RANGE_Y)
    #     wall = Wall()
    #     wall.create_wall(x, y)
    #     wall_list.append(wall)
    #     wall2 = Wall()
    #     wall2.create_wall(int(x+constants.WALL_SIZE), y)
    #     wall_list.append(wall2)
    #     wall3 = Wall()
    #     wall3.create_wall(int(x+constants.WALL_SIZE*2), y)
    #     wall_list.append(wall3)
    # create obstacles type 1
    # for _ in range(3): 
    #     x = random.randint(0, constants.RANGE_X)
    #     y = random.randint(0, constants.RANGE_Y)
    #     wall = Wall()
    #     wall.create_wall(x, y)
    #     wall_list.append(wall)
    #     wall2 = Wall()
    #     wall2.create_wall(int(x+constants.WALL_SIZE), y)
    #     wall_list.append(wall2)
    #     wall3 = Wall()
    #     wall3.create_wall(int(x+constants.WALL_SIZE), int(y+constants.WALL_SIZE))
    #     wall_list.append(wall3)
    cast["walls"] = wall_list

    # CREATE TARGETS
    target_list = []

    for _ in range(constants.BLOCK_COUNT): 
        x = random.randint(0, constants.RANGE_X)
        y = random.randint(0, constants.RANGE_Y)
        target = Target()
        target.create_target(x, y)
        target_list.append(target)
    cast["targets"] = target_list
    
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
    output_service.open_window("The Office Adventure");
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
