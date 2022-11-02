# Import libraries
import random
import pyray as pr

#import service classes
from game_classes.services.keyboard_service import KeyboardService
from game_classes.services.video_service import VideoService

#import shared classes
from game_classes.shared.postion_point import PositionPoint
from game_classes.shared.color import Color

#import actor classes
from game_classes.casting.point_score import PointScore
from game_classes.casting.basket import Basket
from game_classes.casting.game_objects import GameObjects
from game_classes.casting.rocks import Rocks
from game_classes.casting.gems import Gems
from game_classes.casting.object_lists import ObjectLists

#import game loop (director class)
from game_classes.game_loop import Game_loop

#set global attributes/arguments
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color (255, 255, 255)
DEFAULT_FALLING_OBJECTS = 10

#define falling object creation function
def createFallingObject(objectType, ratio, listObject):
    for n in range(DEFAULT_FALLING_OBJECTS/ratio):
        #create object's starting postion and size
        xObject = random.randint(1, COLS -1)
        yObject = random.randint(1, ROWS -1)
        position = PositionPoint(xObject,yObject)
        position = position.scale(CELL_SIZE)
        #create object's color
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color = Color(r, g, b)
        #create object
        fallingObject =  objectType()
        fallingObject.set_font_size(FONT_SIZE)
        fallingObject.set_color(color)
        fallingObject.set_position(position)
        #add to objects lists
        listObject.add_object(f"{objectType}", fallingObject)

#define main function
def main():
    '''The main function that is the entry point of the game. It runs the game_loop and establishes the attributes needed for game play.'''
    #create object lists to create the falling objects, add and remove them
    objects = ObjectLists()

    #create the score display
    score = PointScore()
    score.set_text("")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(PositionPoint(CELL_SIZE, 0))
    #add to object list for drawing
    objects.add_object("score", score)

    #create basket
    #basket starting postion
    x = int(MAX_X/2)
    y = int(MAX_Y/2)
    start_position = PositionPoint(x,y)
    #basket creation
    basket = Basket()
    basket.set_text("#")
    basket.set_font_size(FONT_SIZE)
    basket.set_color(WHITE)
    basket.set_position(start_position)
    #add basket to object list for drawing
    objects.add_object("basket", basket)

    #create rock objects
    createFallingObject("Rock", 2, objects)

    #create gem objects
    createFallingObject("Gems", 1, objects)

    #start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Game_loop(keyboard_service, video_service)
    director.start_game(objects)

#call main function
if __name__ == "__main__":
    main()