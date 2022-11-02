#equivalent to Artifact() class in RFK
from game_classes.casting.game_objects import Game_object


class Rocks(Game_object):
    """
    An item that deducts point. 
    
    The responsibility of a Gem is to give a negative score (value) when catched by the basket.

    Attributes:
        _value (integer): 
    """

    def __init__(self):
        super().__init__()
        self._value = """any negative integer"""
    pass

    def get_value(self):
        """Gets the point of the rock.
        
        Returns:
            integer: negative integer.
        """
        return self._value