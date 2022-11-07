from game_classes.shared.postion_point import PositionPoint
#imported main so that I can use the function createFallingObject()
import __main__

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
        #create 4 gems and 4 rocks before the loop begins
        __main__.createFallingObject("rock", 4, object_list, "O")
        __main__.createFallingObject("gem", 4, object_list, "*")
        #pyray needs to be on a while loop to stay open
        #speed of while loop depends on the frame rate (check __main__)
        while self._window_service.is_window_open():
            #this is a looping counter
            #this while loop is dependent on the frame rate
            #this will serve as a timer or clock
            #counter will count from 1 to 60
            if counter % 60 == 0:
                counter = 0
            counter += 1
            if counter % 30 == 0:
                #add 4 gems and 4 rocks after every 30th count
                __main__.createFallingObject("rock", 2, object_list, "O")
                __main__.createFallingObject("gem", 4, object_list, "*")
            #move all gems and rocks every 10th count
            if counter % 10 == 0:
                self._move_falling_objects(object_list, "rock")
                self._move_falling_objects(object_list, "gem")
            self._get_inputs(object_list)
            self._do_updates(object_list)
            self._do_outputs(object_list)

        self._window_service.close_window()

    #function to move falling objects downward gems and rocks
    def _move_falling_objects(self, object_list, falling_type):
        max_x = self._window_service.get_width()
        max_y = self._window_service.get_height()
        # in here I used object_list._game_objects[falling_type] in order directly access the object_list and edit
        # object_list.get_all_actors() simply wouldn't work since it will return just the copy of the object
        for gem in object_list._game_objects[falling_type]:
            gem.set_velocity(PositionPoint(0, 15))
            gem.move_next(max_x, max_y)
            ypos = gem._position.get_y()
            #if a falling object reached the bottom it will be removed
            if ypos >= 580:
                object_list.remove_game_object(falling_type, gem)

    def _get_inputs(self, object_list):
        """Gets directional input from the keyboard and applies it to the basket.
        
        Args:
            cast (object_list): The cast of objects (the score display, the gems, the rocks and  the basket).
        """
        #gets the user's input to know where to move the basket
        #disabled up and down movement of the basket for now
        basket = object_list.get_first_game_object("basket")
        velocity = self._keyboard.get_direction()
        basket.set_velocity(velocity) 

    def _do_updates(self, object_list):
        """Updates the basket's position and resolves any collisions with artifacts.
        
        Args:
            cast (object_list): The list of objects
        """
        max_x = self._window_service.get_width()
        max_y = self._window_service.get_height()
        score = object_list.get_first_game_object("score")
        basket = object_list.get_first_game_object("basket")
        rocks = object_list._game_objects["rock"]
        #rocks2 = object_list._game_objects["rocks"]
        gems = object_list._game_objects["gem"]
        
        #making the basket move based on user inputs
        #up and down movement of the basket disabled
        basket.move_next(max_x, max_y)

        for type in [rocks, gems]:
            for falling in type:
                if basket.get_position().equals(falling.get_position()):
                    earned_score = falling.get_value()
                    score.set_game_objects_value(earned_score)
                    score.set_text(f'Score: {score.get_game_objects_value()}')
                    type.remove(falling)               

    def _do_outputs(self, object_list):
        """Draws the object_list on the screen.
        
        Args:
            cast (object_list): The cast of actors.
        """
        #collect all game objects and print in on the screen
        listed_objects = object_list.get_all_game_objects()
        self._window_service.clear_buffer()
        self._window_service.draw_objectList(listed_objects)
        self._window_service.flush_buffer()
        



    
