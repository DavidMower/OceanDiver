# settings.py
import pygame


# global variable declarations
global environementImages, environementMapping, outsideDecoMapping, characterImages, currentImage, FPSClock, displaySurf, FPS
global windowWidth, windowHeight, halfWindowWidth, halfWindowHeight, defaultFontSize, defaultFont, outsideDecorationPCT
global maxHealthDiver, maxOxygenDiver, tileWidth, tileHeight, tileFloorHeight, cameraMoveSpeed, displaySurf


# init screen
pygame.init()
FPS = 60 # frames per second to update the screen
windowWidth = 1200 # width of the display surface in pixels
windowHeight = 800 # height of the display surface in pixels
halfWindowWidth = int(windowWidth / 2)
halfWindowHeight = int(windowHeight / 2)
FPSClock = pygame.time.Clock()
displaySurf = pygame.display.set_mode((windowWidth, windowHeight))


# init fonts
defaultFontSize = 18
defaultFont = pygame.font.Font('freesansbold.ttf', defaultFontSize) 


# init colours       R    G    B
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
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
maxHealthDiver = 75 # how much health the player starts with
maxOxygenDiver = 75 # how much oxygen the player starts with


# init level
outsideDecorationPCT = 20 # The percentage of outdoor tiles that have additional decoration on them, such as a tree or rock.
tileWidth = 50 # The total width and height of each tile in pixels.
tileHeight = 85
tileFloorHeight = 40
cameraMoveSpeed = 5 # how many pixels per frame the camera moves
levelIsComplete = False
currentImage = 0 # currentImage is the index of the player's current player image.

# A global dictionary that'll contain all the Pygame Surface objects
environmentImages = {'corner': pygame.image.load('Images/Dark_Rock_Block.png'),
                      'wall': pygame.image.load('Images/Rock_Block.png'),
                      'ocean floor': pygame.image.load('Images/Ocean_Block.png'),
                      'outside floor': pygame.image.load('Images/Sand_Block.png'),
                      'diver_female': pygame.image.load('Images/Scuba_Diver_Female.png'),
                      'diver_male': pygame.image.load('Images/Scuba_Diver_Male.png'),
                      'rock': pygame.image.load('Images/Rock.png'),
                      'short tree': pygame.image.load('Images/Tree_Short.png'),
                      'tall tree': pygame.image.load('Images/Tree_Tall.png'),
                      'ugly tree': pygame.image.load('Images/Tree_Ugly.png')}
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
characterImages = [   environmentImages['diver_female'],
                      environmentImages['diver_male']]