import os
import time
import random
import pygame

# declaring some basic colors to be used throughout the program
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# declaring font location
SI_FONT_LOC = "fonts/spaceFont.ttf"

# screen dimension
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 896

# create screen dimension tuple
SCREEN = (SCREEN_WIDTH, SCREEN_HEIGHT)

# set FPS of the game
FPS = 10

# set the speed of the cannon
CANNON_SPEED = 10

# set the invader and mysteryship movement speed
INVADER_SPEED = 5
THE_MYSTERY_SHIP_SPEED = 5

# verbose output ?
VERBOSE = False