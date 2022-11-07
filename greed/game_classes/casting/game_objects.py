#import needed classes
#equivalent to Actor() class in RFK
from game_classes.shared.postion_point import PositionPoint
from game_classes.shared.color import Color

class GameObjects:
    ''' A visible, moveable thing that participates in the game.
    
    Responsiblity: to keep track of it's appearance, postion and velocity in 2D space.
    
    Attributes:
        _text (string)'''

    def __init__(self):
        """Constructs a new Game Object."""
        self._text = ""
        self._game_objects_value = 0
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = PositionPoint(0, 0)
        self._velocity = PositionPoint(0, 0)

    def get_color(self):
        """Gets the Game Object's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The Game Object's text color.
        """
        return self._color
    
    def get_game_objects_value(self):
        """Gets the Game Object's score value.
        
        Returns:
            integer: Accumulated score
        """
        return self._game_objects_value

    def get_font_size(self):
        """Gets the Game Object's font size.
        
        Returns:
            Point: The Game Object's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the Game Object's position in 2d space.
        
        Returns:
            Point: The Game Object's position in 2d space.
        """
        return self._position

    def get_text(self):
        """Gets the Game Object's textual representation.
        
        Returns:
            string: The Game Object's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the Game Object's speed and direction.
        
        Returns:
            Point: The Game Object's speed and direction.
        """
        return self._velocity

    def auto_move_down():
        pass

    def move_next(self, max_x, max_y):
        """Moves the Game Object to its next position according to its velocity. 

        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = PositionPoint(x, y)

    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_game_objects_value(self, new_score):
        """Updates the score value .
        
        Args:
            integer: the updated score value.
        """
        self._game_objects_value += new_score


    def set_position(self, position):
            """Updates the position to the given one.
            
            Args:
                position (Point): The given position.
            """
            self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.
        
        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity