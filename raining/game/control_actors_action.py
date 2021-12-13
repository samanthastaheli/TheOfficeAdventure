from game.action import Action
from game import constants
from game.point import Point

class ControlActorsAction(Action):
    def __init__(self, input_service) -> None:
        super().__init__()
        self._input_service = input_service


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        player = cast["player"][0] 
        player.set_velocity(direction.scale(constants.PLAYER_SPEED))   
        targets = cast["targets"]
        for target in targets:
            target.set_velocity(Point(0,constants.TARGET_SPEED))   