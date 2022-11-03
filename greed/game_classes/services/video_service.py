#import needed libraries
import pyray as pr

class WindowService:
    '''Outputs the game state.

    Responsibility: to control the game window and draw the game objects
    '''
    def __init__(self, caption, width, height, square_size, frame_rate, debug = False):
        ''' Constructs a new WindowService using the specified debug mode.
        
        Args:
            caption (string): the caption to be displayed
            width (int): the width of the window displayed
            height (int): the height of the window displayed.
            square_size (int): the size of the square of the game grid.
            frams_rate (int): the rate of frame refresh and speed of the game.
            debug (bool): whether or not to draw in debug mode.
            '''
        #declare self variables and attributes from arguments
        pass

    def close_window(self):
        ''' Closes the window and releases all computing resources
        '''
        pass

    def clear_buffer(self):
        '''Clears the buffer in preparation for the next rendering. this method should be called at the beginning of the game's output phase
        '''
        pass

    def draw_object(self, object):
        '''Draws the given object's text on the screen.
        
        Args:
            object (Game_object or a child class of Game_object: the object to be drawn on the screen.
        '''
        pass

    def draw_objectList(self, objectList):
        ''' Draws the objects in the given list of objects.
        
        Args:
            objectList (list): a list of objects to draw.
        '''
        pass

    def flush_buffer(self):
        ''' Copies the buffer contents to the screen. This method should be called at the end of the game's output phase.
        '''
        pass

    def get_square_size(self):
        '''Get's the video screen's square size.
        
        Returns:
            Gird: the video screen's square size.
        '''
        pass

    def get_height(self):
        '''Gets the video screen's height.
        
        Returns:
            Grid: the video screen's height.
        '''
        pass

    def get_width(self):
        ''' Gets the video screen's width
        
        Returns:
            Grid: the video screen's width
        '''
        pass

    def is_window_open(self):
        ''' Whether or not the window was closed by the user.
        
        Returns:
            bool: True if the window is closing: False if otherwise.
        '''
        pass

    def open_window(self):
        ''' Opens a new window with the provided caption.
        
        Args:
            caption (string): the caption provided to be the title.
        '''
        pass

    def _draw_grid(self):
        '''Draws a grid ont he screen. Used for debugging purposes
        '''
        pass
