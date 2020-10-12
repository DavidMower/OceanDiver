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
BLACK     = (0  , 0  , 0)
DARKGREY  = (40 , 40 , 40)
LIGHTGREY = (100, 100, 100)
GREEN     = (0  , 255, 0)
RED       = (255, 0  , 0)
YELLOW    = (255, 255, 0)
BLUE      = (0  , 128, 255)
DARKBLUE   = (0  , 102, 255)


# game settings
WIDTH      = 1024 # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT     = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS        = 60
TITLE      = "Ocean Diver"
SHOW_FTP   = True
DRAW_GRID  = False
BGCOLOR    = BLUE
TILESIZE   = 64
GRIDWIDTH  = WIDTH / TILESIZE # this value is how many squares show on the screen
GRIDHEIGHT = HEIGHT / TILESIZE # this value is how many squares show on the screen

# HUD settings
BAR_LENGTH = 100
BAR_HEIGHT = 20

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
                    'diver_male_10': pg.image.load('Images/Player/diver_male_10.png'),
                    'turtle_01': pg.image.load('Images/AquaticLife/Turtle/turtle_01.png'),
                    'turtle_02': pg.image.load('Images/AquaticLife/Turtle/turtle_02.png'),
                    'turtle_03': pg.image.load('Images/AquaticLife/Turtle/turtle_03.png'),
                    'turtle_04': pg.image.load('Images/AquaticLife/Turtle/turtle_04.png'),
                    'turtle_05': pg.image.load('Images/AquaticLife/Turtle/turtle_05.png'),
                    'turtle_06': pg.image.load('Images/AquaticLife/Turtle/turtle_06.png'),
                    'turtle_07': pg.image.load('Images/AquaticLife/Turtle/turtle_07.png'),
                    'turtle_08': pg.image.load('Images/AquaticLife/Turtle/turtle_08.png'),
                    'turtle_09': pg.image.load('Images/AquaticLife/Turtle/turtle_09.png'),
                    'rock_01': pg.image.load('Images/Levels/Decorations/Rock2.png')
                    }

# Player settings
PLAYER_SPEED     = 175 # degrees per second
PLAYER_ROT_SPEED = 80 # degrees per second
PLAYER_ANIMATION_SPEED = 6 # higher is slower
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
                    IMAGES_TO_LOAD['diver_male_10']
                    ]
PLAYER_HEALTH = 1000
PLAYER_OXYGEN = 1000

# map decoration settings
ROCK_IMAGES =   [IMAGES_TO_LOAD['rock_01']
                ]

# Sea Turtle settings
TURTLE_SPEED     = 30 # degrees per second
TURTLE_ROT_SPEED = 30 # degrees per second
TURTLE_ANIMATION_SPEED = 8 # higher is slower
TURTLE_IMG       = IMAGES_TO_LOAD['turtle_01'] # sets the initial turtle image, before any movement
TURTLE_HIT_RECT  = pg.Rect(0, 0, 80, 80)
TURTLE_IMAGES    = [IMAGES_TO_LOAD['turtle_01'],
                    IMAGES_TO_LOAD['turtle_02'],
                    IMAGES_TO_LOAD['turtle_03'],
                    IMAGES_TO_LOAD['turtle_04'],
                    IMAGES_TO_LOAD['turtle_05'],
                    IMAGES_TO_LOAD['turtle_06'],
                    IMAGES_TO_LOAD['turtle_07'],
                    IMAGES_TO_LOAD['turtle_08'],
                    IMAGES_TO_LOAD['turtle_09']
                    ]
TURTLE_HEALTH = 5000
TURTLE_DAMAGE = 1
TURTLE_KNOCKBACK = 10