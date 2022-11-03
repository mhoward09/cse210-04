#import needed libraries
import pyray as pr

#import needed classes
from game_classes.shared.postion_point import PositionPoint

class Keyboard:
    ''' Detects player keyboard input

    Responsibility: detect player key presses and translate them into a PositionPoint representing a direction (left or right).

    Attributes:
        square_size (int): for scaling directional input to a grid
    '''
    def __init__(self, square_size = 1):
        ''' Constructs a new Keyboard using the specified square size.

        Args:
            square_size (int): the size of a square in the display grid.
        '''
        #declare self variables and attributes from arguments
        pass

    def get_direction(self):
        ''' Gets the selected direction based on the currently pressed keys.

        Returns:
            PositionPoint: the selected direction
        '''
        pass
