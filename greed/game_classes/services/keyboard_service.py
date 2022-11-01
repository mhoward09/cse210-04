#import needed libraries
import pyray as pr

#import needed classes
from game_classes.shared.postion_point import PositionPoint

class KeyboardService:
    ''' Detects player keyboard input

    Responsibility: detect player key presses and translate them into a PositionPoint representing a direction (left or right).

    Attributes:
        cell_size (int): for scaling directional input to a grid
    '''
    def __init__(self, cell_size):
        ''' Constructs a new Keyboard Service using the specified cell size.

        Args:
            cell_size (int): the size of a cell in the display grid.
        '''
        #declare self variables and attributes from arguments
        pass

    def get_direction(self):
        ''' Gets the selected direction based on the currently pressed keys.

        Returns:
            PositionPoint: the selected direction
        '''
        pass