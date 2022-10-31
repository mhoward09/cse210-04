"# cse210-04" 
# Greed
A game of skill. Can you get the most points by catching the gems in your basket? Beware the rocks. They will lower your score.

# System requirements
Python 3.8.0 ore newer
Raylib Python CFFI 3.7

root
+-- greed
    +-- game_classes                            (game classes)
        +-- shared                              (classes shared by all objects)
            +-- position_point                  (class definning the point object)
            +-- color                           (class defining the color object)
        +-- actors                              (classes of game objects)
            +-- falling_objects                 (parent class for gems and rocks)
            +-- gems                            (class for gems)
            +-- rocks                           (class for rocks)
            +-- basket                          (class for the catching basket)
            +-- point_score                     (class for score keeping)
        +-- services                            (classes of game control mechanics)
            +-- keyboard_service                (game controls)
            +-- video_service                   (game window control)
        +-- game_loop                           (director of game play)
    +--__main__.py                              (entry point)
+--README.me                                    (general info)