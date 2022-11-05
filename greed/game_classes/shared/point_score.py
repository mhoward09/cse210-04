class PointScore:
    ''' A child class of GameObjects. This class holds and maintains the player score.

    Responsibility: to hold and provide information about the player's score. It contains a method to update the score based on what the basket catches.
    
    Attributes:
        all attributes in the GameObjects class
        _value (int): the value of the how many points have been scored by the player
    '''

    def __init__(self):
        '''Creates a new score object'''
        #call a super and add a _value attribute
        super().__init__()
        self._value = 0


    def get_value(self):
        '''Returns the value stored in self._value'''
        return self._value