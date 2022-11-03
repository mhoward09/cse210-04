class Game_loop:
    ''' The loop that directs game play.

        Responsibility: control the sequence of play.

        Attributes:
            _keyboard_ (Keyboard): for getting directional input to
                move the basket.
            _window_service (windowService): for providing video output
    '''
    def __init__(self, keyboard, window_service):
        ''' Consturcts a new loop using the specified keyboard and video services.

            Args:
                keyboard (Keyboard): an instance of the
                    Keyboard class.
                window_service (WindowService): an instance of the WindowService class.
        '''
        #declaring self variables from the given arguments
        self._keyboard = keyboard
        self._window_service = window_service
        
    def start_game(self, object_list):
        ''' Stats the game using the given list of objects. Runs the main game loop.

            Args:
                object_list (ObjectList): the objects for game play.
        '''
        counter = 0
        #windowService method to open window for game play
        self._window_service.open_window()
        #game loop that runs while the window is open
        while self._window_service.is_window_open():
            self._get_inputs(object_list)
            self._do_updates(object_list)
            self._do_outputs(object_list)

            #this is a looping counter
            #this while loop is dependent on the frame rate
            #I need a looping counter based on the frame rate
            #I might use it or might not use it 
            #but I'll keep it here just in case
            counter += 1
            if counter % 12 == 0:
                counter = 0

        self._window_service.close_window()

    def _get_inputs(self, object_list):
        """Gets directional input from the keyboard and applies it to the basket.
        
        Args:
            cast (object_list): The cast of objects (the score display, the gems, the rocks and  the basket).
        """
        robot = object_list.get_first_game_object("robots")
        velocity = self._keyboard.get_direction()
        robot.set_velocity(velocity) 
        pass  

    def _do_updates(self, object_list):
        """Updates the basket's position and resolves any collisions with artifacts.
        
        Args:
            cast (object_list): The list of objects
        """
        cast = object_list
        score = cast.get_first_actor("score")
        basket = cast.get_first_actor("basket")
        fallingObject = cast.get_actors("fallingObject")

        score.set_text("Score: %s" % score.get_value())
        max_x = self._window_service.get_width()
        max_y = self._window_service.get_height()
        basket.move_next(max_x, max_y)
        
        for gameObject in fallingObject:
            if basket.get_position().equals(gameObject.get_position()):
                scoreValue = score.get_value() + gameObject.get_value()
                score.set_text(scoreValue)    

    def _do_outputs(self, object_list):
        """Draws the object_list on the screen.
        
        Args:
            cast (object_list): The cast of actors.
        """
        self._window_service.clear_buffer()
        listed_objects = object_list.get_all_game_objects()
        self._window_service.draw_objectList(listed_objects)
        self._window_service.flush_buffer()
        pass

    
