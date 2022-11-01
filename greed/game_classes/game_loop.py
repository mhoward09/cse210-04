class Game_loop:
    ''' The loop that directs game play.

        Responsibility: control the sequence of play.

        Attributes:
            _keyboard_service (KeyboardService): for getting directional input to
                move the basket.
            _video_service (VideoService): for providing video output
    '''
    def __init__(self, keyboard_service, video_service):
        ''' Consturcts a new loop using the specified keyboard and video services.

            Args:
                keyboard_service (KeyboardService): an instance of the
                    KeyboardService class.
                video_service (VideoService): an instance of the VideoService class.
        '''
        #declaring self variables from the given arguments
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, object_list):
        ''' Stats the game using the given list of objects. Runs the main game loop.

            Args:
                object_list (ObjectList): the objects for game play.
        '''
        #VideoService method to open window for game play
        self._video_service.open_window()
        #game loop that runs while the window is open
        while self._video_service.is_window_open():
            pass

    