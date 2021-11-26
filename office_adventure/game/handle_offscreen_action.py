import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class HandleOffScreenAction(Action):
    """A code template for handling when player goes off screen. 
    The responsibility of this class is so make the player change directions when gets to off screen points.
    """
    def __init__(self, cast):
        super().__init__()
        self._cast = cast

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        player = cast["players"][0]