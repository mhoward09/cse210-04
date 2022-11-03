#import needed libraries
import pyray 

class windowService:
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
        self._caption = caption
        self._width = width
        self._height = height
        self._square_size = square_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        ''' Closes the window and releases all computing resources
        '''
         pyray.close_window()

    def clear_buffer(self):
        '''Clears the buffer in preparation for the next rendering. this method should be called at the beginning of the game's output phase
        '''
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()

    def draw_object(self, object):
        '''Draws the given object's text on the screen.
        
        Args:
            object (Game_object or a child class of Game_object: the object to be drawn on the screen.
        '''
        text = object.get_text()
        x = object.get_position().get_x()
        y = object.get_position().get_y()
        font_size = object.get_font_size()
        color = object.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)

    def draw_objectList(self, objectList):
        ''' Draws the objects in the given list of objects.
        
        Args:
            objectList (list): a list of objects to draw.
        '''
        for object in objectList:
            self.draw_object(object)

    def flush_buffer(self):
        ''' Copies the buffer contents to the screen. This method should be called at the end of the game's output phase.
        '''
        pyray.end_drawing()

    def get_square_size(self):
        '''Get's the video screen's square size.
        
        Returns:
            Gird: the video screen's square size.
        '''
        return self._square_size

    def get_height(self):
        '''Gets the video screen's height.
        
        Returns:
            Grid: the video screen's height.
        '''
        return self._height

    def get_width(self):
        ''' Gets the video screen's width
        
        Returns:
            Grid: the video screen's width
        '''
        return self._width

    def is_window_open(self):
        ''' Whether or not the window was closed by the user.
        
        Returns:
            bool: True if the window is closing: False if otherwise.
        '''
        return not pyray.window_should_close()

    def open_window(self):
        ''' Opens a new window with the provided caption.
        
        Args:
            caption (string): the caption provided to be the title.
        '''
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    def _draw_grid(self):
        '''Draws a grid ont he screen. Used for debugging purposes
        '''
        for y in range(0, self._height, self._square_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._square_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)
