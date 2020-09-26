#####################################################
##                   settings.py                   ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame, pygame_menu, os
import level
from player import *

global environmentImages, environmentMapping, outsideDecoMapping, characterImages, currentImage, FPSClock, displaySurf, FPS
global windowWidth, windowHeight, halfWindowWidth, halfWindowHeight, defaultFontSize, defaultFont, outsideDecorationPCT
global tileWidth, tileHeight, tileFloorHeight, cameraMoveSpeed, displaySurf

# init screen
pygame.init()
FPS = 60 # frames per second to update the screen
windowWidth      = 1200 # width of the display surface in pixels
windowHeight     = 800 # height of the display surface in pixels
halfWindowWidth  = int(windowWidth / 2)
halfWindowHeight = int(windowHeight / 2)
FPSClock = pygame.time.Clock()
displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
# init fonts
defaultFontSize = 18
defaultFont = pygame.font.Font('freesansbold.ttf', defaultFontSize)
colourBlack      = (  0,   0,   0)
colourBlue       = (  0,   0, 128)
colourGreen      = (  0, 255,   0)
colourRed        = (155,   0,   0)
colourWhite      = (255, 255, 255)
colourYellow     = (155, 155,   0)
colourBrightBlue = (  0, 170, 255)
textBGColour     = colourBrightBlue
textColour       = colourWhite
# init player character
UP      = 'up'
DOWN    = 'down'
LEFT    = 'left'
RIGHT   = 'right'
player1 = Player("maleCharacter"  , 300, 300, 75, 75) # create player1 using Player class (name, startx, starty, health, oxygen)
player2 = Player("femaleCharacter", 300, 300, 75, 75) # create player1 using Player class (name, startx, starty, health, oxygen)
# init level
outsideDecorationPCT = 20 # The percentage of outdoor tiles that have additional decoration on them, such as a tree or rock.
tileWidth            = 50 # The total width and height of each tile in pixels.
tileHeight           = 85
tileHeightChar       = 300
tileFloorHeight      = 40
cameraMoveSpeed      = 40 # how many pixels per frame the camera moves
levelIsComplete      = False
# Read in the levels from the text file. See the readLevelsFile() for details on the format of this file
levels = level.readLevelsFile('Levels/CoastalDive.lvl')
currentLevelIndex = 0
# A global dictionary that'll contain all the Pygame Surface objects
environmentImages = { 'corner':        pygame.image.load('Images/Dark_Rock_Block.png'),
                      'wall':          pygame.image.load('Images/Rock_Block.png'),
                      'ocean floor':   pygame.image.load('Images/Level/ocean_tile_1.png'),
                      'outside floor': pygame.image.load('Images/Sand_Block.png'),
                      'diver_female':  pygame.image.load('Images/Scuba_Diver_Female.png'),
                      'diver_male_01': pygame.image.load('Images/Player/diver_male_01.png'),
                      'diver_male_02': pygame.image.load('Images/Player/diver_male_02.png'),
                      'diver_male_03': pygame.image.load('Images/Player/diver_male_03.png'),
                      'diver_male_04': pygame.image.load('Images/Player/diver_male_04.png'),
                      'diver_male_05': pygame.image.load('Images/Player/diver_male_05.png'),
                      'diver_male_06': pygame.image.load('Images/Player/diver_male_06.png'),
                      'diver_male_07': pygame.image.load('Images/Player/diver_male_07.png'),
                      'diver_male_08': pygame.image.load('Images/Player/diver_male_08.png'),
                      'diver_male_09': pygame.image.load('Images/Player/diver_male_09.png'),
                      'diver_male_10': pygame.image.load('Images/Player/diver_male_10.png'),
                      'rock':          pygame.image.load('Images/Rock.png'),
                      'short tree':    pygame.image.load('Images/Tree_Short.png'),
                      'tall tree':     pygame.image.load('Images/Tree_Tall.png'),
                      'ugly tree':     pygame.image.load('Images/Tree_Ugly.png')}
# These dictionary values are global, and map the character that appear in the level file
environmentMapping = {'x': environmentImages['corner'],
                      '#': environmentImages['wall'],
                      'o': environmentImages['ocean floor'],
                      ' ': environmentImages['outside floor']}
outsideDecoMapping = {'1': environmentImages['rock'],
                      '2': environmentImages['short tree'],
                      '3': environmentImages['tall tree'],
                      '4': environmentImages['ugly tree']}
# characterImages is a list of all possible characters the player can be.
characterImages = [ environmentImages['diver_male_01'],
                    environmentImages['diver_male_02'],
                    environmentImages['diver_male_03'],
                    environmentImages['diver_male_04'],
                    environmentImages['diver_male_05'],
                    environmentImages['diver_male_06'],
                    environmentImages['diver_male_07'],
                    environmentImages['diver_male_08'],
                    environmentImages['diver_male_09'],
                    environmentImages['diver_male_10']]
currentImage = 0 # currentImage is the index of the player's current player image.
# menu images
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
menuUnderwaterBGBlank = os.path.join(os.path.dirname(full_path), 'Images', 'Menu', 'UnderwaterBGBlank.png')
menuOceanDiver = os.path.join(os.path.dirname(full_path), 'Images', 'Menu', 'oceandiver.jpg')