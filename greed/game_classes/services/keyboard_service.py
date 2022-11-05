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
        self._cell_size = square_size


    def get_direction(self):
        ''' Gets the selected direction based on the currently pressed keys.

        Returns:
            PositionPoint: the selected direction
        '''
        dx = 0
        dy = 0

        if pr.is_key_down(pr.KEY_LEFT):
            dx = -1
        
        if pr.is_key_down(pr.KEY_RIGHT):
            dx = 1
        
        if pr.is_key_down(pr.KEY_UP):
            dy = -1
        
        if pr.is_key_down(pr.KEY_DOWN):
            dy = 1

        #enable up and down movement: direction = PositionPoint(dx, dy)
        #disable up and down movement
        direction = PositionPoint(dx, 0)
        #scaled to specify the length of movement because dx dy is a unitless direction
        direction = direction.scale(self._cell_size)
        
        return direction
