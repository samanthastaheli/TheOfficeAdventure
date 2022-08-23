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

from game.level_factory import LevelFactory
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
    cast["placeholders"] = []
    cast["walls"] = []
    cast["levels"] = []
    cast["obstacles"] = []
    cast["text"] = []

    level = LevelFactory()

    # build all actors
    level.build_walls()
    level.build_desk()
    level.build_targets()
    level.build_player()
    level.build_placeholders()

    # append to cast dict
    cast["walls"] = level.get_walls()
    cast["obstacles"] = level.get_obstacles()
    cast["targets"] = level.get_targets()
    cast["player"] = level.get_player()
    cast["placeholders"] = level.get_placeholders()
    
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
