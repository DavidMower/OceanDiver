#####################################################
##                    level.py                     ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame, os, random, copy, time
import settings, player
from main import *


def readLevelsFile(aFileName):
    """ reads a level text file which can contain any of the following characters

    |------------------------------------------------|
    |  Level element         |  Character            |
    |------------------------------------------------|
    |  Wall                  |  #                    |
    |  Player                |  @                    |
    |  Player on goal square |  +                    |
    |  Box                   |  $                    |
    |  Box on goal square    |  *                    |
    |  Goal square           |  .                    |
    |  Floor                 |  (Space)              |
    |------------------------------------------------|

    Args:
        aFileName ([lvl]): [level text file]

    Returns:
        [levels]: [levels object containing all levels read]
    """
    assert os.path.exists(aFileName), 'Cannot find the level file: %s' % (aFileName)
    mapFile = open(aFileName, 'r')
    content = mapFile.readlines() + ['\r\n'] # Each level must end with a blank line
    mapFile.close()

    levels = [] # Will contain a list of level objects.
    levelNum = 0
    mapTextLines = [] # contains the lines for a single level's map.
    mapObj = [] # the map object made from the data in mapTextLines
    for lineNum in range(len(content)): # Process each line in the level file.
        line = content[lineNum].rstrip('\r\n')
        if ';' in line: # Ignore the ; lines, they're comments in the level file.
            line = line[:line.find(';')]
        if line != '': # Finding the lines which are part of the map.
            mapTextLines.append(line)
        elif line == '' and len(mapTextLines) > 0:
            # A blank line indicates the end of a level's map in the file.
            # Convert the text in mapTextLines into a level object.
            # Find the longest row in the map.
            maxWidth = -1
            for i in range(len(mapTextLines)):
                if len(mapTextLines[i]) > maxWidth:
                    maxWidth = len(mapTextLines[i])
            # Add spaces to the ends of the shorter rows. This ensures the map will be rectangular.
            for i in range(len(mapTextLines)):
                mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))
            # Convert mapTextLines to a map object.
            for x in range(len(mapTextLines[0])):
                mapObj.append([])
            for y in range(len(mapTextLines)):
                for x in range(maxWidth):
                    mapObj[x].append(mapTextLines[y][x])
            # Loop through the spaces in the map and find the @, ., and $
            # characters for the starting game state.
            settings.player1.setStartX(None) # x for the player's starting position
            settings.player1.setStartY(None) # y for the player's starting position
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@', '+'):
                        # '@' is player, '+' is player & goal
                        settings.player1.setStartX(x)
                        settings.player1.setStartY(y)
            # Basic level design sanity checks:
            assert settings.player1.getStartX != None and settings.player1.getStartY != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, aFileName)
            # Create game state object
            gameStateObj = {'player': (settings.player1.getStartX(), settings.player1.getStartY()),
                            'health': settings.player1.getHealth(),
                            'oxygen': settings.player1.getOxygen()
                            }
            # Create level object
            levelObj = {'width'     : maxWidth,
                        'height'    : len(mapObj),
                        'mapObj'    : mapObj,
                        'startState': gameStateObj}
            levels.append(levelObj)
            # Finally, reset the variables for reading the next map.
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelNum += 1
    return levels

def decorateMap(mapObj, startxy):
    """ Makes a copy of the given map object and modifies it.
    Walls that are corners are turned into corner pieces.
    The outside/inside floor tile distinction is made.
    Tree/rock decorations are randomly added to the outside tiles.

    Args:
        mapObj ([mapObj]): [map object]
        startxy ([startxy]): [start coordinates value including x and y]

    Returns:
        [map]: [returns the decorated map object.]
    """
    settings.player1.getStartX, settings.player1.getStartY = startxy # Syntactic sugar
    mapObjCopy = copy.deepcopy(mapObj) # Copy the map object so we don't modify the original passed
    # Remove the non-wall characters from the map data as we've already created the level object, we are just decorating that level here
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):
                mapObjCopy[x][y] = ' '
    # Flood fill to determine inside/outside floor tiles
    floodFill(mapObjCopy, settings.player1.getStartX, settings.player1.getStartY, ' ', 'o')
    # Convert the adjoined walls into corner tiles
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] == '#':
                if (isWall(mapObjCopy, x, y-1) and isWall(mapObjCopy, x+1, y)) or \
                   (isWall(mapObjCopy, x+1, y) and isWall(mapObjCopy, x, y+1)) or \
                   (isWall(mapObjCopy, x, y+1) and isWall(mapObjCopy, x-1, y)) or \
                   (isWall(mapObjCopy, x-1, y) and isWall(mapObjCopy, x, y-1)):
                    mapObjCopy[x][y] = 'x'
            elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < settings.outsideDecorationPCT:
                mapObjCopy[x][y] = random.choice(list(settings.outsideDecoMapping.keys()))
    return mapObjCopy

def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    """ Changes any values matching oldCharacter on the map object to
    newCharacter at the (x, y) position, and does the same for the
    positions to the left, right, down, and up of (x, y), recursively.

    The flood fill algorithm creates the inside/outside floor distinction. This is a "recursive" function.
    For more info on the Flood Fill algorithm, see: http://en.wikipedia.org/wiki/Flood_fill

    Args:
        mapObj ([type]): [description]
        x ([type]): [description]
        y ([type]): [description]
        oldCharacter ([type]): [description]
        newCharacter ([type]): [description]
    """
    if mapObj[x][y] == oldCharacter:
        mapObj[x][y] = newCharacter
    if x < len(mapObj) - 1 and mapObj[x+1][y] == oldCharacter:
        floodFill(mapObj, x+1, y, oldCharacter, newCharacter) # call right
    if x > 0 and mapObj[x-1][y] == oldCharacter:
        floodFill(mapObj, x-1, y, oldCharacter, newCharacter) # call left
    if y < len(mapObj[x]) - 1 and mapObj[x][y+1] == oldCharacter:
        floodFill(mapObj, x, y+1, oldCharacter, newCharacter) # call down
    if y > 0 and mapObj[x][y-1] == oldCharacter:
        floodFill(mapObj, x, y-1, oldCharacter, newCharacter) # call up


def isWall(mapObj, x, y):
    """ Checks if object is a wall

    Args:
        mapObj ([mapObj]): [the loaded level in a mapObj]
        x ([int]): [x position of the character]
        y ([int]): [y position of the character]

    Returns:
        [boolean]: [Returns True if the (x, y) position on the map is a wall, otherwise return False.]
    """
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False # x and y aren't actually on the map.
    elif mapObj[x][y] in ('#', 'x'):
        return True # wall is blocking
    return False

def isBlocked(mapObj, gameStateObj, x, y):
    """ Check if the possible move would be blocked, or not.

    Args:
        mapObj ([mapObj]): [the loaded level in a mapObj]
        gameStateObj ([gameStateObj]): [the current game state]
        x ([int]): [x position of the character]
        y ([int]): [y position of the character]

    Returns:
        [boolean]: [Returns True if the (x, y) position on the map is blocked by a wall or star, otherwise return False.]
    """
    if isWall(mapObj, x, y):
        return True
    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True # x and y aren't actually on the map.
    return False

def drawMap(mapObj, gameStateObj):
    """ Draws the map to a Surface object, including the player and stars.
    This function does not call pygame.display.update(), nor
    does it draw the "Level" and "Steps" text in the corner.

    Args:
        mapObj ([mapObj]): [the loaded level in a mapObj]
        gameStateObj ([gameStateObj]): [the current game state]

    Returns:
        [mapSurf]: [the single Surface object that the tiles are drawn on]
    """
    # mapSurf will be the single Surface object that the tiles are drawn
    # on, so that it is easy to position the entire map on the displaySurf
    # Surface object. First, the width and height must be calculated.
    mapSurfWidth = len(mapObj) * settings.tileWidth
    mapSurfHeight = (len(mapObj[0]) - 1) * settings.tileFloorHeight + settings.tileHeight
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(settings.textBGColour) # start with a blank color on the surface.
    # Draw the tile sprites onto this surface.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect        = pygame.Rect((x * settings.tileWidth, y * settings.tileFloorHeight, settings.tileWidth, settings.tileHeight))
            spaceRectForChar = pygame.Rect((x * settings.tileWidth, y * settings.tileFloorHeight, settings.tileWidth, settings.tileHeightChar))
            if mapObj[x][y] in settings.environmentMapping:
                baseTile = settings.environmentMapping[mapObj[x][y]]
            elif mapObj[x][y] in settings.outsideDecoMapping:
                baseTile = settings.environmentMapping[' ']
            # First draw the base ground/wall tile.
            mapSurf.blit(baseTile, spaceRect)
            if mapObj[x][y] in settings.outsideDecoMapping:
                # Draw any tree/rock decorations that are on this tile.
                mapSurf.blit(settings.outsideDecoMapping[mapObj[x][y]], spaceRect)
            # Last draw the player on the board.
            if (x, y) == gameStateObj['player']:
                mapSurf.blit(settings.characterImages[settings.currentImage], spaceRectForChar) # currentImage refers to a key in "characterImages" which has the specific player image
    return mapSurf

def drawCharacterNextImage():
    """ Change the player image to the next one.
    After the last player image, use the first one.
    """
    settings.currentImage += 1
    if settings.currentImage >= len(settings.characterImages):
        settings.currentImage = 0
    mapNeedsRedraw = True

def runLevel(levels, levelNum):
    """ Run a level

    Args:
        levels ([levels]): [levels object containing all the loaded levels]
        levelNum ([int]): [level number]

    Returns:
        [boolean]: [Is the level solved, or not]
    """
    # level initialisations
    levelObj = levels[levelNum]
    mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
    gameStateObj = copy.deepcopy(levelObj['startState'])
    mapNeedsRedraw = True # set to True to call drawMap()
    levelSurf = settings.defaultFont.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, settings.textColour)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (60, 30) # position of level text
    mapWidth = len(mapObj) * settings.tileWidth
    mapHeight = (len(mapObj[0]) - 1) * settings.tileFloorHeight + settings.tileHeight
    Max_Cam_X_Pan = abs(settings.halfWindowHeight - int(mapHeight / 2)) + settings.tileWidth
    Max_Cam_Y_Pan = abs(settings.halfWindowWidth - int(mapWidth / 2)) + settings.tileHeight
    # Track how much the camera has moved:
    cameraOffsetX = 0
    cameraOffsetY = 0
    # Track if the keys to move the camera are being held down:
    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False
    while True: # main game loop
        playerMoveTo = None # ensure this is always reset
        for event in pygame.event.get(): # event handling loop
            keyPressed  = False
            cameraLeft  = False
            cameraRight = False
            cameraUp    = False
            cameraDown  = False
            if event.type == QUIT: # Player clicked the "X" at the corner of the window.
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    keyPressed = True
                    playerMoveTo = settings.LEFT
                    cameraLeft  = True
                    drawCharacterNextImage()
                elif event.key == K_RIGHT:
                    keyPressed = True
                    playerMoveTo = settings.RIGHT
                    cameraRight  = True
                    drawCharacterNextImage()
                elif event.key == K_UP:
                    keyPressed = True
                    playerMoveTo = settings.UP
                    cameraUp  = True
                    drawCharacterNextImage()
                elif event.key == K_DOWN:
                    keyPressed = True
                    playerMoveTo = settings.DOWN
                    cameraDown  = True
                    drawCharacterNextImage()
                elif event.key == K_n:
                    return 'next'
                elif event.key == K_b:
                    return 'back'
                elif event.key == K_ESCAPE: # Esc key quits
                    terminate()
                elif event.key == K_BACKSPACE: # Reset the level
                    return 'reset'
                else: # to cover if no key is now being pressed
                    keyPressed  = False
            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    keyPressed  = False
                    cameraLeft  = False
                elif event.key == K_RIGHT:
                    keyPressed  = False
                    cameraRight = False
                elif event.key == K_UP:
                    keyPressed  = False
                    cameraUp    = False
                elif event.key == K_DOWN:
                    keyPressed  = False
                    cameraDown  = False
        if playerMoveTo != None and not settings.levelIsComplete:
            # If the player pushed a key to move, make the move
            # (if possible) and push any objects that are pushable.
            moved = player.makeMove(mapObj, gameStateObj, playerMoveTo)
            if moved:
                mapNeedsRedraw = True
        settings.displaySurf.fill(settings.textBGColour)
        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj)
            mapNeedsRedraw = False
        playerx, playery = gameStateObj['player']
        if cameraUp and cameraOffsetY < Max_Cam_X_Pan:
            cameraOffsetY += settings.cameraMoveSpeed
        elif cameraDown and cameraOffsetY > -Max_Cam_X_Pan:
            cameraOffsetY -= settings.cameraMoveSpeed
        if cameraLeft and cameraOffsetX < Max_Cam_Y_Pan:
            cameraOffsetX += settings.cameraMoveSpeed
        elif cameraRight and cameraOffsetX > -Max_Cam_Y_Pan:
            cameraOffsetX -= settings.cameraMoveSpeed
        # Adjust mapSurf's Rect object based on the camera offset.
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (settings.halfWindowWidth + cameraOffsetX, settings.halfWindowHeight + cameraOffsetY)
        # draw mapSurf to the display Surf Surface object so the level is displayed in the background
        settings.displaySurf.blit(mapSurf, mapSurfRect)
        # draw levelSurf to display the level indicator
        settings.displaySurf.blit(levelSurf, levelRect)
        # draw the player health and oxygen bars
        drawHealthBar(settings.player1.getHealth())
        drawOxygenBar(settings.player1.getOxygen())
        if settings.levelIsComplete:
            # is solved, show the "Solved!" image until the player has pressed a key.
            solvedRect = settings.environmentImages['sand'].get_rect()
            solvedRect.center = (settings.halfWindowWidth, settings.halfWindowHeight)
            settings.displaySurf.blit(settings.environmentImages['sand'], solvedRect)
            if keyPressed == True:
                return 'solved'
        pygame.display.update() # draw displaySurf to the screen.
        settings.FPSClock.tick()