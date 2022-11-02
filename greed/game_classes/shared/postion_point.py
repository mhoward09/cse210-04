class PositionPoint:
    ''' A distance from a relative origin (0,0).

    Respsonibility: to hold and provide information about itself.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    '''
    def __init__(self, x, y):
        ''' Create a new position point using the specified x and y values.

        Args:
            x (int): the specified x value.
            y (int): the specified y value.
        '''
        #declare self variables from given arguments
        self._x = x
        self._y = y

    def add(self, other):
        ''' Gets a new point that is the sum of this point and a given point.

        Args:
            other (PositionPoint): the point to add to the initial point
        
        Returns:
            Point: the new point made from the sum of the two points
        '''
        #add two points mathematically
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return PositionPoint(x, y)

    def equals(self, other):
        ''' Compares this point with another to see if they are equal (being equal is a collision or catch).

        Args:
            other (PositionPoint): the point used for comparison.

        Returns:
            boolean: True if both x and y are equal: False if otherwise.
        '''
        #compare two points 
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        ''' Gets the horizontal distance.

        Returns:
            integer: the horizontal distance from the origin
        '''
        #return x value
        return self._x

    def get_y(self):
        ''' Gets the vertical distance.

        Returns:
            integer: the vertical distance from the origin
        '''
        #return y value
        return self._y

    def scale(self, factor):
        ''' Scales the point by the provided factor.

        Args:
            factor (int): the amount to scale by.

        Returns:
            PositionPoint: A new point that has been scaled.
        '''
        #return value of point that has been multiplied by a factor
        return PositionPoint(self._x * factor, self._y * factor)