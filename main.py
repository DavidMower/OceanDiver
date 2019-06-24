# main.py

# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 
import random, sys, copy, os, pygame
from pygame.locals import *
from settings import *


def main():
    # pygame initialisation
    pygame.init()
    pygame.display.set_caption('Scuba Diver')
    
    showMainMenu() # show the title screen until the user presses a key

    # Read in the levels from the text file. See the readLevelsFile() for details on the format of this file
    levels = readLevelsFile('Levels/CoastalDive.lvl')
    currentLevelIndex = 0

    # The main game loop. This loop runs a single level, when the user finishes that level, the next/previous level is loaded.
    while True:
        # Run the level to actually start playing the game:
        result = runLevel(levels, currentLevelIndex)

        if result in ('solved', 'next'):
            # Go to the next level.
            currentLevelIndex += 1
            if currentLevelIndex >= len(levels):
                # If there are no more levels, go back to the first one.
                currentLevelIndex = 0
        elif result == 'back':
            # Go to the previous level.
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                # If there are no previous levels, go to the last one.
                currentLevelIndex = len(levels)-1
        elif result == 'reset':
            pass # Do nothing. Loop re-calls runLevel() to reset the level


def runLevel(levels, levelNum):
    # level initialisations
    levelObj = levels[levelNum]
    mapObj = decorateMap(levelObj['mapObj'], levelObj['startState']['player'])
    gameStateObj = copy.deepcopy(levelObj['startState'])
    mapNeedsRedraw = True # set to True to call drawMap()
    levelSurf = defaultFont.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, textColour)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (60, 30) # position of level text
    mapWidth = len(mapObj) * tileWidth
    mapHeight = (len(mapObj[0]) - 1) * tileFloorHeight + tileHeight
    Max_Cam_X_Pan = abs(halfWindowHeight - int(mapHeight / 2)) + tileWidth
    Max_Cam_Y_Pan = abs(halfWindowWidth - int(mapWidth / 2)) + tileHeight

    # Track how much the camera has moved:
    cameraOffsetX = 0
    cameraOffsetY = 0
    # Track if the keys to move the camera are being held down:
    cameraUp = False
    cameraDown = False
    cameraLeft = False
    cameraRight = False

    while True: # main game loop
        # Reset these variables:
        playerMoveTo = None
        keyPressed = False
        
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                # Player clicked the "X" at the corner of the window.
                terminate()

            elif event.type == KEYDOWN:
                # Handle key presses
                keyPressed = True
                if event.key == K_LEFT:
                    playerMoveTo = LEFT
                elif event.key == K_RIGHT:
                    playerMoveTo = RIGHT
                elif event.key == K_UP:
                    playerMoveTo = UP
                elif event.key == K_DOWN:
                    playerMoveTo = DOWN

                # Set the camera move mode.
                elif event.key == K_a:
                    cameraLeft = True
                elif event.key == K_d:
                    cameraRight = True
                elif event.key == K_w:
                    cameraUp = True
                elif event.key == K_s:
                    cameraDown = True

                elif event.key == K_n:
                    return 'next'
                elif event.key == K_b:
                    return 'back'

                elif event.key == K_ESCAPE:
                    terminate() # Esc key quits.
                elif event.key == K_BACKSPACE:
                    return 'reset' # Reset the level.
                elif event.key == K_p:
                    # Change the player image to the next one.
                    currentImage += 1
                    if currentImage >= len(characterImages):
                        # After the last player image, use the first one.
                        currentImage = 0
                    mapNeedsRedraw = True

            elif event.type == KEYUP:
                # Unset the camera move mode.
                if event.key == K_a:
                    cameraLeft = False
                elif event.key == K_d:
                    cameraRight = False
                elif event.key == K_w:
                    cameraUp = False
                elif event.key == K_s:
                    cameraDown = False

        if playerMoveTo != None and not levelIsComplete:
            # If the player pushed a key to move, make the move
            # (if possible) and push any stars that are pushable.
            moved = makeMove(mapObj, gameStateObj, playerMoveTo)

            if moved:
                # increment the step counter.
                gameStateObj['stepCounter'] += 1
                mapNeedsRedraw = True

        displaySurf.fill(textBGColour)

        if mapNeedsRedraw:
            mapSurf = drawMap(mapObj, gameStateObj)
            mapNeedsRedraw = False

        if cameraUp and cameraOffsetY < Max_Cam_X_Pan:
            cameraOffsetY += cameraMoveSpeed
        elif cameraDown and cameraOffsetY > -Max_Cam_X_Pan:
            cameraOffsetY -= cameraMoveSpeed
        if cameraLeft and cameraOffsetX < Max_Cam_Y_Pan:
            cameraOffsetX += cameraMoveSpeed
        elif cameraRight and cameraOffsetX > -Max_Cam_Y_Pan:
            cameraOffsetX -= cameraMoveSpeed

        # Adjust mapSurf's Rect object based on the camera offset.
        mapSurfRect = mapSurf.get_rect()
        mapSurfRect.center = (halfWindowWidth + cameraOffsetX, halfWindowHeight + cameraOffsetY)

        # draw mapSurf to the display Surf Surface object so the level is displayed in the background
        displaySurf.blit(mapSurf, mapSurfRect)
        # draw levelSurf to display the level indicator
        displaySurf.blit(levelSurf, levelRect)
        # draw the player health and oxygen bars
        drawHealthBar(gameStateObj['health'])
        drawOxygenBar(gameStateObj['oxygen'])

        if levelIsComplete:
            # is solved, show the "Solved!" image until the player
            # has pressed a key.
            solvedRect = environmentImages['sand'].get_rect()
            solvedRect.center = (halfWindowWidth, halfWindowHeight)
            displaySurf.blit(environmentImages['sand'], solvedRect)

            if keyPressed:
                return 'solved'

        pygame.display.update() # draw displaySurf to the screen.
        FPSClock.tick()
        

# creates the Surface and Rect objects for some text
def writeText(aText, aColour, aBackgroundColour, aTop, aLeft):
    textSurf = defaultFont.render(aText, True, aColour, aBackgroundColour)
    textRect = textSurf.get_rect()
    textRect.topleft = (aTop, aLeft)
    return (textSurf, textRect)
        

# creates a health bar
def drawHealthBar(currentDiverHealth):
    for c in range(currentDiverHealth): # draw the red health bars
        pygame.draw.rect(displaySurf, colourRed, (15, 20 + (10 * maxHealthDiver) - c * 10, 20, 10))
    for m in range(maxHealthDiver):
        pygame.draw.rect(displaySurf, colourBlack, (15, 20 + (10 * maxHealthDiver) - m * 10, 20, 10), 1)
    healthBarSurf, healthBarRect = writeText('H', colourGreen, colourBlue, 5, 5)
    healthBarSurf.blit(healthBarSurf, healthBarRect)


# creates a oxygen bar
def drawOxygenBar(currentDiverOxygen):
    for c in range(currentDiverOxygen): # draw the blue oxygen bars 
        pygame.draw.rect(displaySurf, colourBlue, (windowWidth - 35, 25 + (10 * maxOxygenDiver) - c * 10, 20, 10))
    for m in range(maxOxygenDiver):
        pygame.draw.rect(displaySurf, colourBlack, (windowWidth - 35, 25 + (10 * maxOxygenDiver) - m * 10, 20, 10), 1)
    oxygenBarSurf, oxygenBarRect = writeText('O', colourGreen, colourBlue, 20, 20)
    oxygenBarSurf.blit(oxygenBarSurf, oxygenBarRect)


# checks if object is a wall
def isWall(mapObj, x, y):
    """Returns True if the (x, y) position on
    the map is a wall, otherwise return False."""
    if x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return False # x and y aren't actually on the map.
    elif mapObj[x][y] in ('#', 'x'):
        return True # wall is blocking
    return False


# corners made, inside/outside seperated and decorations added to the outside
def decorateMap(mapObj, startxy):
    """Makes a copy of the given map object and modifies it.
        * Walls that are corners are turned into corner pieces.
        * The outside/inside floor tile distinction is made.
        * Tree/rock decorations are randomly added to the outside tiles.
    Returns the decorated map object."""

    startx, starty = startxy # Syntactic sugar

    # Copy the map object so we don't modify the original passed
    mapObjCopy = copy.deepcopy(mapObj)

    # Remove the non-wall characters from the map data
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):
                mapObjCopy[x][y] = ' '

    # Flood fill to determine inside/outside floor tiles
    floodFill(mapObjCopy, startx, starty, ' ', 'o')

    # Convert the adjoined walls into corner tiles
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] == '#':
                if (isWall(mapObjCopy, x, y-1) and isWall(mapObjCopy, x+1, y)) or \
                   (isWall(mapObjCopy, x+1, y) and isWall(mapObjCopy, x, y+1)) or \
                   (isWall(mapObjCopy, x, y+1) and isWall(mapObjCopy, x-1, y)) or \
                   (isWall(mapObjCopy, x-1, y) and isWall(mapObjCopy, x, y-1)):
                    mapObjCopy[x][y] = 'x'

            elif mapObjCopy[x][y] == ' ' and random.randint(0, 99) < outsideDecorationPCT:
                mapObjCopy[x][y] = random.choice(list(outsideDecoMapping.keys()))
    return mapObjCopy


def isBlocked(mapObj, gameStateObj, x, y):
    """Returns True if the (x, y) position on the map is
    blocked by a wall or star, otherwise return False."""

    if isWall(mapObj, x, y):
        return True

    elif x < 0 or x >= len(mapObj) or y < 0 or y >= len(mapObj[x]):
        return True # x and y aren't actually on the map.

    elif (x, y) in gameStateObj['stars']:
        return True # a star is blocking

    return False


# move player if possible
def makeMove(mapObj, gameStateObj, playerMoveTo):
    """Given a map and game state object, see if it is possible for the
    player to make the given move. If it is, then change the player's
    position (and the position of any pushed star). If not, do nothing.
    Returns True if the player moved, otherwise False."""

    # Make sure the player can move in the direction they want.
    playerx, playery = gameStateObj['player']

    # The code for handling each of the directions is so similar aside
    # from adding or subtracting 1 to the x/y coordinates. We can
    # simplify it by using the xOffset and yOffset variables.
    if playerMoveTo == UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == RIGHT:
        xOffset = 1
        yOffset = 0
    elif playerMoveTo == DOWN:
        xOffset = 0
        yOffset = 1
    elif playerMoveTo == LEFT:
        xOffset = -1
        yOffset = 0

    # See if the player can move in that direction.
    if isWall(mapObj, playerx + xOffset, playery + yOffset):
        return False
    else:
        # Move the player upwards.
        gameStateObj['player'] = (playerx + xOffset, playery + yOffset)
        return True

# waits for any key to be pressed
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

# main menu loop
def showMainMenu():
    while True:
        displaySurf.fill(colourWhite)

        # start playing main-menu music
        pygame.mixer.music.load('Sounds/MainMenu.flac')
        pygame.mixer.music.play(-1, 0.0)

        # draw the main menu title text
        mainTitleSurf, mainTitleRect = writeText('Scuba Diver', colourGreen, colourBlue, windowWidth - 612, windowHeight - 620)
        displaySurf.blit(mainTitleSurf, mainTitleRect)

        # draw the main menu buttons
        newGameSurf, newGameRect       = writeText('Start New Game', colourBlack, colourWhite, windowWidth - 612, windowHeight - 520)
        displaySurf.blit(newGameSurf, newGameRect)
        loadGameSurf, loadGameRect     = writeText(  'Load Game',    colourBlack, colourWhite, windowWidth - 612, windowHeight - 470)
        displaySurf.blit(loadGameSurf, loadGameRect)
        saveGameSurf, saveGameRect     = writeText(  'Save Game',    colourBlack, colourWhite, windowWidth - 612, windowHeight - 420)
        displaySurf.blit(saveGameSurf, saveGameRect)
        howToPlaySurf, howToPlayRect   = writeText( 'How to Play',   colourBlack, colourWhite, windowWidth - 612, windowHeight - 370)
        displaySurf.blit(howToPlaySurf, howToPlayRect)
        optionsSurf, optionsRect       = writeText(   'Options',     colourBlack, colourWhite, windowWidth - 612, windowHeight - 320)
        displaySurf.blit(optionsSurf, optionsRect)
        highScoresSurf, highScoresRect = writeText( 'High Scores',   colourBlack, colourWhite, windowWidth - 612, windowHeight - 270)
        displaySurf.blit(highScoresSurf, highScoresRect)
        quitSurf, quitRect             = writeText(    'Quit',       colourBlack, colourWhite, windowWidth - 612, windowHeight - 220)
        displaySurf.blit(quitSurf, quitRect)

        # temp loop so I can test the menu
        if checkForKeyPress():
            # launch the select level menu
            showLevelMenu()
            pygame.event.get() # clear event queue
            return

        pygame.display.update()
        FPSClock.tick(FPS)


# level menu loop
def showLevelMenu():
    while True:
        displaySurf.fill(colourWhite)

        # draw the level menu title text
        levelMenuTitleSurf, levelMenuTitleRect = writeText('Level select', colourGreen, colourBlue, windowWidth - 612, windowHeight - 620)
        displaySurf.blit(levelMenuTitleSurf, levelMenuTitleRect)

        # draw the level menu buttons
        menuCoastalSurf, menuCoastalRect       = writeText('  (1) Coastal Dive',   colourBlack, colourWhite, windowWidth - 612, windowHeight - 520)
        displaySurf.blit(menuCoastalSurf, menuCoastalRect)
        menuCoralReefSurf, menuCoralReefRect   = writeText(' (2) Coral Reef Dive', colourBlack, colourWhite, windowWidth - 612, windowHeight - 470)
        displaySurf.blit(menuCoralReefSurf, menuCoralReefRect)
        menuWreckSurf, menuWreckRect           = writeText('   (3) Wreck Dive',    colourBlack, colourWhite, windowWidth - 612, windowHeight - 420)
        displaySurf.blit(menuWreckSurf, menuWreckRect)
        menuCaveSurf, menuCaveRect             = writeText('   (4) Cave Dive',     colourBlack, colourWhite, windowWidth - 612, windowHeight - 370)
        displaySurf.blit(menuCaveSurf, menuCaveRect)
        menuMangroveSurf, menuMangroveRect     = writeText('  (5) Mangrove Dive',  colourBlack, colourWhite, windowWidth - 612, windowHeight - 320)
        displaySurf.blit(menuMangroveSurf, menuMangroveRect)
        menuAntarcticaSurf, menuAntarcticaRect = writeText( '(6) Antarctica Dive', colourBlack, colourWhite, windowWidth - 612, windowHeight - 270)
        displaySurf.blit(menuAntarcticaSurf, menuAntarcticaRect)

        # temp loop so I can test the menu
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            pygame.mixer.music.stop() # stop the main menu background music
            return
            
        pygame.display.update()
        FPSClock.tick(FPS)


def readLevelsFile(aFileName):
    assert os.path.exists(aFileName), 'Cannot find the level file: %s' % (aFileName)
    mapFile = open(aFileName, 'r')
    # Each level must end with a blank line
    content = mapFile.readlines() + ['\r\n']
    mapFile.close()

    levels = [] # Will contain a list of level objects.
    levelNum = 0
    mapTextLines = [] # contains the lines for a single level's map.
    mapObj = [] # the map object made from the data in mapTextLines
    for lineNum in range(len(content)):
        # Process each line that was in the level file.
        line = content[lineNum].rstrip('\r\n')

        if ';' in line:
            # Ignore the ; lines, they're comments in the level file.
            line = line[:line.find(';')]

        if line != '':
            # This line is part of the map.
            mapTextLines.append(line)
        elif line == '' and len(mapTextLines) > 0:
            # A blank line indicates the end of a level's map in the file.
            # Convert the text in mapTextLines into a level object.

            # Find the longest row in the map.
            maxWidth = -1
            for i in range(len(mapTextLines)):
                if len(mapTextLines[i]) > maxWidth:
                    maxWidth = len(mapTextLines[i])
            # Add spaces to the ends of the shorter rows. This
            # ensures the map will be rectangular.
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
            startx = None # The x and y for the player's starting position
            starty = None
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@', '+'):
                        # '@' is player, '+' is player & goal
                        startx = x
                        starty = y

            # Basic level design sanity checks:
            assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, aFileName)

            # Create level object and starting game state object.
            gameStateObj = {'player': (startx, starty),
                            'stepCounter': 0,
                            'health': maxHealthDiver,
                            'oxygen': maxOxygenDiver}

            levelObj = {'width': maxWidth,
                        'height': len(mapObj),
                        'mapObj': mapObj,
                        'startState': gameStateObj}

            levels.append(levelObj)

            # Reset the variables for reading the next map.
            mapTextLines = []
            mapObj = []
            gameStateObj = {}
            levelNum += 1
    return levels


def floodFill(mapObj, x, y, oldCharacter, newCharacter):
    """Changes any values matching oldCharacter on the map object to
    newCharacter at the (x, y) position, and does the same for the
    positions to the left, right, down, and up of (x, y), recursively."""

    # In this game, the flood fill algorithm creates the inside/outside
    # floor distinction. This is a "recursive" function.
    # For more info on the Flood Fill algorithm, see:
    #   http://en.wikipedia.org/wiki/Flood_fill
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


def drawMap(mapObj, gameStateObj):
    """Draws the map to a Surface object, including the player and
    stars. This function does not call pygame.display.update(), nor
    does it draw the "Level" and "Steps" text in the corner."""

    # mapSurf will be the single Surface object that the tiles are drawn
    # on, so that it is easy to position the entire map on the displaySurf
    # Surface object. First, the width and height must be calculated.
    mapSurfWidth = len(mapObj) * tileWidth
    mapSurfHeight = (len(mapObj[0]) - 1) * tileFloorHeight + tileHeight
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(textBGColour) # start with a blank color on the surface.

    # Draw the tile sprites onto this surface.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((x * tileWidth, y * tileFloorHeight, tileWidth, tileHeight))
            if mapObj[x][y] in environmentMapping:
                baseTile = environmentMapping[mapObj[x][y]]
            elif mapObj[x][y] in outsideDecoMapping:
                baseTile = environmentMapping[' ']

            # First draw the base ground/wall tile.
            mapSurf.blit(baseTile, spaceRect)

            if mapObj[x][y] in outsideDecoMapping:
                # Draw any tree/rock decorations that are on this tile.
                mapSurf.blit(outsideDecoMapping[mapObj[x][y]], spaceRect)

            # Last draw the player on the board.
            if (x, y) == gameStateObj['player']:
                # Note: The value "currentImage" refers to a key in "characterImages" which has the specific player image we want to show.
                mapSurf.blit(characterImages[currentImage], spaceRect)
    return mapSurf


# terminates the game when called
def terminate():
    pygame.quit()
    sys.exit()


# start the main() loop function
if __name__ == '__main__':
    main()