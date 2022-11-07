#equivalent to Artifact() class in RFK
from game_classes.casting.game_objects import GameObjects


class Rocks(GameObjects):
    """
    An item that deducts point. 
    
    The responsibility of a Gem is to give a negative score (value) when catched by the basket.

    Attributes:
        _value (integer): 
    """

    def __init__(self):
        super().__init__()
        self._value = int(-10)


    def get_value(self):
        """Gets the point of the rock.
        
        Returns:
            integer: negative integer.
        """
        return self._value