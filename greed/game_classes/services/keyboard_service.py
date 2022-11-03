#import needed libraries
import pyray 

#import needed classes
from game_classes.shared.position_point import PositionPoint

class key_board:
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
         self._square_size = square_size

    def get_direction(self):
        ''' Gets the selected direction based on the currently pressed keys.

        Returns:
            PositionPoint: the selected direction
        '''
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_UP):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = 1

        direction = PositionPoint(dx, dy)
        direction = direction.scale(self._square_size)
        
        return direction
