#equivalent to Artifact() class in RFK
from game_classes.casting.game_objects import GameObjects


class Gems(GameObjects):
    """
    An item that adds point. 
    
    The responsibility of a Gem is to give a positive score (value) when catched by the basket.

    Attributes:
        _value (integer): 
    """

    def __init__(self):
        super().__init__()
        self._value = int(10)


    def get_value(self):
        """Gets the point of the gem.
        
        Returns:
            integer: positive integer.
        """
        return self._value