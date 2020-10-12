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

# images settings
IMAGES_TO_LOAD = {  'diver_male_01': pg.image.load('Images/Player/diver_male_01.png'),
                    'diver_male_02': pg.image.load('Images/Player/diver_male_02.png'),
                    'diver_male_03': pg.image.load('Images/Player/diver_male_03.png'),
                    'diver_male_04': pg.image.load('Images/Player/diver_male_04.png'),
                    'diver_male_05': pg.image.load('Images/Player/diver_male_05.png'),
                    'diver_male_06': pg.image.load('Images/Player/diver_male_06.png'),
                    'diver_male_07': pg.image.load('Images/Player/diver_male_07.png'),
                    'diver_male_08': pg.image.load('Images/Player/diver_male_08.png'),
                    'diver_male_09': pg.image.load('Images/Player/diver_male_09.png'),
                    'diver_male_10': pg.image.load('Images/Player/diver_male_10.png')}

# Player settings
PLAYER_SPEED     = 175 # degrees per second
PLAYER_ROT_SPEED = 80 # degrees per second
PLAYER_ANIMATION_SPEED = 8
PLAYER_IMG       = IMAGES_TO_LOAD['diver_male_01'] # sets the initial character image, before any movement
PLAYER_HIT_RECT  = pg.Rect(0, 0, 80, 80)
PLAYER_IMAGES    = [IMAGES_TO_LOAD['diver_male_01'],
                    IMAGES_TO_LOAD['diver_male_02'],
                    IMAGES_TO_LOAD['diver_male_03'],
                    IMAGES_TO_LOAD['diver_male_04'],
                    IMAGES_TO_LOAD['diver_male_05'],
                    IMAGES_TO_LOAD['diver_male_06'],
                    IMAGES_TO_LOAD['diver_male_07'],
                    IMAGES_TO_LOAD['diver_male_08'],
                    IMAGES_TO_LOAD['diver_male_09'],
                    IMAGES_TO_LOAD['diver_male_10']]