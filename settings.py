#####################################################
##                   settings.py                   ##
##                   Ocean Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 3.8.2 32-bit              ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame as pg
from os import path

# set some directory settings
GAME_FOLDER       = path.dirname(__file__)
IMG_FOLDER        = path.join(GAME_FOLDER, 'Images')
PLAYER_IMG_FOLDER = path.join(IMG_FOLDER, 'Player')

# define some colors (R, G, B)
WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
DARKGREY  = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN     = (0, 255, 0)
RED       = (255, 0, 0)
YELLOW    = (255, 255, 0)

# game settings
WIDTH      = 1024 # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT     = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS        = 60
TITLE      = "Ocean Diver"
BGCOLOR    = DARKGREY
TILESIZE   = 64
GRIDWIDTH  = WIDTH / TILESIZE # this value is how many squares show on the screen
GRIDHEIGHT = HEIGHT / TILESIZE # this value is how many squares show on the screen

# Player settings
PLAYER_SPEED     = 250 # degrees per second
PLAYER_ROT_SPEED = 120 # degrees per second
PLAYER_IMG       = 'diver_male_01.png'
PLAYER_HIT_RECT  = pg.Rect(0, 0, 90, 90)
PLAYER_IMAGES    = ['diver_male_01.png',
                    'diver_male_02.png',
                    'diver_male_03.png',
                    'diver_male_04.png',
                    'diver_male_05.png',
                    'diver_male_06.png',
                    'diver_male_07.png',
                    'diver_male_08.png',
                    'diver_male_09.png',
                    'diver_male_10.png']