class Color:
    ''' A color as designated by RGB scale.

    Responsibility: To hold and provide information about itself.

    Attributes:
        _red (int): the red value.
        _green (int): the green value.
        _blue (int): the blue value.
        _alpha (int): the opacity of the color.
    '''

    def __init__(self, red, green, blue, alpha = 255):
        ''' Constructs a new color using the specified RGB and alpha values. 

        Args:
            red (int): the red value.
            green (int): the green value.
            blue (int): the blue value
            alpha (int): the alpha value or opacity of the color.
        '''
        #declare self variables from arguments
        pass

    def to_tuple(self):
        ''' Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple (int, int, int, int): the color as a tuple
        '''
        pass