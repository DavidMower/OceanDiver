#####################################################
##                     main.py                     ##
##                   Ocean Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 2.7.18 64-bit             ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import os, sys, math, copy, random, pygame, pygame_menu

# main init
pygame.init()
pygame.display.set_caption('Ocean Diver')
screen = pygame.display.set_mode((1280, 800))
rect = screen.get_rect()
clock = pygame.time.Clock()

# set some paths
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

# create some colours
colourWhite      = (255, 255, 255)
colourRed        = (155,   0,   0)
colourBlack      = (  0,   0,   0)
colourBlue       = (  0,   0, 128)
colourGreen      = (  0, 255,   0)
colourWhite      = (255, 255, 255)
colourYellow     = (155, 155,   0)
colourBrightBlue = (  0, 170, 255)

# create some fonts
defaultFontSize = 18
defaultFont = pygame.font.Font('freesansbold.ttf', defaultFontSize)

# level init
outsideDecorationPCT = 20 # The percentage of outdoor tiles that have additional decoration on them, such as a tree or rock.
tileWidth            = 50 # The total width and height of each tile in pixels.
tileHeight           = 85
tileHeightChar       = 300
tileFloorHeight      = 40

# A global dictionary that'll contain all the Pygame Surface objects
environmentImages = { 'corner':        pygame.image.load('Images/Levels/Decorations/zrpg-tiles/rock2.png'),
                      'wall':          pygame.image.load('Images/Levels/Decorations/zrpg-tiles/rock1.png'),
                      'ocean floor':   pygame.image.load('Images/Levels/CoastalDive/ocean_tile_1.png'),
                      'outside floor': pygame.image.load('Images/Levels/CoastalDive/sand_block.png'),
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
                      'rock3':         pygame.image.load('Images/Levels/Decorations/zrpg-tiles/rock3.png'),
                      'rock4':         pygame.image.load('Images/Levels/Decorations/zrpg-tiles/rock4.png'),
                      'short tree':    pygame.image.load('Images/Levels/Decorations/Tree_Short.png'),
                      'ugly tree':     pygame.image.load('Images/Levels/Decorations/Tree_Ugly.png')}

# These dictionary values are global, and map the character that appear in the level file
environmentMapping = {'x': environmentImages['corner'],
                      '#': environmentImages['wall'],
                      'o': environmentImages['ocean floor'],
                      ' ': environmentImages['outside floor']}
outsideDecoMapping = {'1': environmentImages['rock3'],
                      '2': environmentImages['short tree'],
                      '3': environmentImages['rock4'],
                      '4': environmentImages['ugly tree']}

# Load images globally and reuse them in your program.
# Also use the `.convert()` or `.convert_alpha()` methods after loading the images to improve the performance.
DIVER1 = pygame.Surface((30, 100), pygame.SRCALPHA)
DIVER1.fill((130, 180, 20))
MARKER1 = pygame.Surface((10, 10), pygame.SRCALPHA)
MARKER1.fill((200, 120, 20))
BACKGROUND = pygame.Surface((1280, 800))
BACKGROUND.fill((30, 30, 30))


class Background(pygame.sprite.Sprite):
    """[summary]

    Args:
        pygame ([type]): [description]
    """
    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)


class Entity(pygame.sprite.Sprite):
        """[summary]

        Args:
            pygame ([type]): [description]
        """
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)


class PlayerSprite(Entity):
    """ Player class for the main character.

    Args:
        Entity ([type]): [description]
    """
    MAX_FORWARD_SPEED = 10
    MAX_REVERSE_SPEED = 2
    ACCELERATION = 0.05
    TURN_SPEED = 0.000000000001
    currentImage = 0 # currentImage is the index of the player's current player image.
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

    def __init__(self, image, position, aHealth, aOxygen):
        """ constructer

        Args:
            image ([type]): [description]
            position ([type]): [description]
        """
        Entity.__init__(self)
        self.src_image = self.characterImages[0]
        self.image     = self.characterImages[self.currentImage]
        self.rect      = self.image.get_rect(center=position)
        self.position  = pygame.math.Vector2(position)
        self.velocity  = pygame.math.Vector2(0, 0)
        self.speed     = self.direction = 0
        self.k_left    = self.k_right = self.k_down = self.k_up = 0
        self.health    = aHealth
        self.oxygen    = aOxygen
        self.startPosX = 0
        self.startPosY = 0

    def getHealth(self):
        """[summary]

        Returns:
            [int]: [players health value]
        """
        return self.health

    def getOxygen(self):
        """[summary]

        Returns:
            [int]: [players oxygen value]
        """
        return self.oxygen

    def getStartX(self):
        """[summary]

        Returns:
            [int]: [players starting x position]
        """
        return self.startPosX

    def setStartX(self, aStartX):
        """[summary]

        Returns:
            [int]: [players starting x position]
        """
        self.startPosX = aStartX

    def getStartY(self):
        """[summary]

        Returns:
            [int]: [players starting y position]
        """
        return self.startPosY

    def setStartY(self, aStartY):
        """[summary]

        Returns:
            [int]: [players starting y position]
        """
        self.startPosX = aStartY

    def update(self, time):
        """[summary]

        Args:
            time ([type]): [description]
        """
        # SIMULATION
        self.speed += self.k_up + self.k_down
        # To clamp the speed.
        self.speed = max(-self.MAX_REVERSE_SPEED,
                        min(self.speed, self.MAX_FORWARD_SPEED))

        # Degrees sprite is facing (direction)
        self.direction += (self.k_right + self.k_left)
        rad = math.radians(self.direction)
        self.velocity.x = -self.speed*math.sin(rad)
        self.velocity.y = -self.speed*math.cos(rad)
        self.position += self.velocity
        self.rect = self.image.get_rect(center=self.position)
        self.image = self.characterImages[self.currentImage]
        self.image = pygame.transform.rotate(self.image, self.direction)

    def drawCharacterNextImage(self):
        """ Cycle through the images for this sprite

        """
        self.currentImage += 1
        if self.currentImage >= len(self.characterImages):
            self.currentImage = 0 # keeps number of sprite images within range
        #mapNeedsRedraw = True


# init for game loop
background = Background(BACKGROUND, [0, 0])
diver = PlayerSprite(DIVER1, rect.center, 100, 100)
start = PlayerSprite(MARKER1, rect.center, 10, 10)


def writeText(aText, aColour, aBackgroundColour, aTop, aLeft):
    """ Creates the Surface and Rect objects to write some text

    Args:
        aText ([string]): [text to be printed]
        aColour ([string]): [font colour]
        aBackgroundColour ([string]): [background colour]
        aTop ([int]): [coordinate value from top of screen]
        aLeft ([int]): [coordinate value from left of screen]

    Returns:
        [textSurf]: [surface text object]
        [textRect]: [rectangle text object]
    """
    textSurf = defaultFont.render(aText, True, aColour, aBackgroundColour)
    textRect = textSurf.get_rect()
    textRect.topleft = (aTop, aLeft)
    return (textSurf, textRect)


def drawHealthBar(aPlayersHealth):
    """ Creates a health bar

    Args:
        aPlayersHealth ([int]): [value for health]
    """
    for eachHealth in range(aPlayersHealth):
        # draw a red health rectangle for each oxygen value
        pygame.draw.rect(screen, colourRed, (15, 20 + (10 * diver.getHealth()) - eachHealth * 10, 20, 10))
    for eachHealth2 in range(diver.getHealth()):
        # draw a black background rectangle for each oxygen value
        pygame.draw.rect(screen, colourBlack, (15, 20 + (10 * diver.getHealth()) - eachHealth2 * 10, 20, 10), 1)
    # write H above the health bar
    healthBarSurf, healthBarRect = writeText('H', colourRed, colourBlack, 18, 5)
    screen.blit(healthBarSurf, healthBarRect)

def drawOxygenBar(aPlayersOxygen):
    """ Creates a oxygen bar.
    Draw a blue oxygen rectangle for each oxygen value.
    Draw a black background rectangle for each oxygen value.
    Print an O above the oxygen bar.

    Args:
        aPlayersOxygen ([int]): [value for oxygen]
    """
    for eachOxygen in range(aPlayersOxygen):
        pygame.draw.rect(screen, colourBrightBlue,  (1280 - 35, 25 + (10 * diver.getOxygen()) - eachOxygen * 10, 20, 10))
    for eachOxygen2 in range(diver.getOxygen()):
        pygame.draw.rect(screen, colourBlack, (1280 - 35, 25 + (10 * diver.getOxygen()) - eachOxygen2 * 10, 20, 10), 1)
    oxygenBarSurf, oxygenBarRect = writeText('O', colourBrightBlue, colourBlack, 1248, 10)
    screen.blit(oxygenBarSurf, oxygenBarRect)

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
            diver.setStartX(None) # x for the player's starting position
            diver.setStartY(None) # y for the player's starting position
            for x in range(maxWidth):
                for y in range(len(mapObj[x])):
                    if mapObj[x][y] in ('@', '+'):
                        # '@' is player, '+' is player & goal
                        diver.setStartX(x)
                        diver.setStartY(y)
            # Basic level design sanity checks:
            assert diver.getStartX != None and diver.getStartY != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, aFileName)
            # Create game state object
            gameStateObj = {'player': (diver.getStartX(), diver.getStartY()),
                            'health': diver.getHealth(),
                            'oxygen': diver.getOxygen()
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

def drawMap(mapObj, gameStateObj):
    """ Draws the map to a Surface object, including the stars.
    This function does not call pygame.display.update(), nor
    does it draw the "Level" and "Steps" text in the corner.

    mapSurf will be the single Surface object that the tiles are drawn
    on, so that it is easy to position the entire map on the display
    Surface object.

    Args:
        mapObj ([mapObj]): [the loaded level in a mapObj]
        gameStateObj ([gameStateObj]): [the current game state]

    Returns:
        [mapSurf]: [the single Surface object that the tiles are drawn on]
    """
    mapSurfWidth = len(mapObj) * tileWidth
    mapSurfHeight = (len(mapObj[0]) - 1) * tileFloorHeight + tileHeight
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(colourYellow) # start with a blank color on the surface.
    # Draw the tile sprites onto this surface.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect        = pygame.Rect((x * tileWidth, y * tileFloorHeight, tileWidth, tileHeight))
            spaceRectForChar = pygame.Rect((x * tileWidth, y * tileFloorHeight, tileWidth, tileHeightChar))
            if mapObj[x][y] in environmentMapping:
                baseTile = environmentMapping[mapObj[x][y]]
            elif mapObj[x][y] in outsideDecoMapping:
                baseTile = environmentMapping[' ']
            # First draw the base ground/wall tile.
            mapSurf.blit(baseTile, spaceRect)
            if mapObj[x][y] in outsideDecoMapping:
                # Draw any tree/rock decorations that are on this tile.
                mapSurf.blit(outsideDecoMapping[mapObj[x][y]], spaceRect)
    return mapSurf

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
    diver.getStartX, diver.getStartY = startxy # Syntactic sugar
    mapObjCopy = copy.deepcopy(mapObj) # Copy the map object so we don't modify the original passed
    # Remove the non-wall characters from the map data as we've already created the level object, we are just decorating that level here
    for x in range(len(mapObjCopy)):
        for y in range(len(mapObjCopy[0])):
            if mapObjCopy[x][y] in ('$', '.', '@', '+', '*'):
                mapObjCopy[x][y] = ' '
    # Flood fill to determine inside/outside floor tiles
    floodFill(mapObjCopy, diver.getStartX, diver.getStartY, ' ', 'o')
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
                #mapObjCopy[x][y] = random.choice(list(outsideDecoMapping.keys()))
                pass
    return mapObjCopy

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
    levelSurf = defaultFont.render('Level %s of %s' % (levelNum + 1, len(levels)), 1, colourRed)
    levelRect = levelSurf.get_rect()
    levelRect.bottomleft = (60, 30) # position of level text
    mapWidth = len(mapObj) * tileWidth
    mapHeight = (len(mapObj[0]) - 1) * tileFloorHeight + tileHeight
    Max_Cam_X_Pan = abs(400 - int(mapHeight / 2)) + tileWidth
    Max_Cam_Y_Pan = abs(640 - int(mapWidth / 2)) + tileHeight
    # Track how much the camera has moved:
    cameraOffsetX = 0
    cameraOffsetY = 0
    # redraw the level each tick
    if mapNeedsRedraw:
        mapSurf = drawMap(mapObj, gameStateObj)
        mapNeedsRedraw = False
    # check if player has completed the level
    #if levelIsComplete:
        # is solved, show the "Solved!" image until the player has pressed a key.
    #    solvedRect = environmentImages['sand'].get_rect()
    #    solvedRect.center = (640, 400)
    #    screen.blit(environmentImages['sand'], solvedRect)
    # draw the level on the screen for this tick
    mapSurfRect = mapSurf.get_rect()
    mapSurfRect.center = (640 + cameraOffsetX, 400 + cameraOffsetY)
    screen.blit(mapSurf, mapSurfRect)
    pygame.display.update()


def main_loop():
    """[summary]

    """
    diver_group = pygame.sprite.Group(diver)
    #start_group = pygame.sprite.Group(start)
    all_sprites = pygame.sprite.Group(diver_group)#, start_group) # will need to add all the fish here

    camera = pygame.math.Vector2(0, 0)
    done = False

    # load the level
    currentLevelIndex = 0
    levelIsComplete   = False
    mapNeedsRedraw = True
    # Read in the levels from the text file. See the readLevelsFile() for details on the format of this file
    levels = readLevelsFile('Levels/CoastalDive.lvl')
    print("Successfully loaded CoastalDive level!")

    # Main loop
    while not done:
        # clear the screen before we start a new frame
        screen.fill(colourYellow)

        # if player has moved, redraw the map
        if mapNeedsRedraw:
            # run the level
            levelResult = runLevel(levels, currentLevelIndex)
            if levelResult in ('solved', 'next'):
                currentLevelIndex += 1
                if currentLevelIndex >= len(levels):
                    currentLevelIndex = 0
            elif levelResult == 'back':
                currentLevelIndex -= 1
                if currentLevelIndex < 0:
                    currentLevelIndex = len(levels)-1
            elif levelResult == 'reset':
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Player clicked the "X" at the corner of the window.
                done = True
            elif event.type == pygame.KEYDOWN: # to cover when a key is pressed
                # Diver Input (Player 1)
                if event.key == pygame.K_RIGHT:
                    diver.k_right = -5
                    mapNeedsRedraw = True
                    diver.drawCharacterNextImage()
                elif event.key == pygame.K_LEFT:
                    diver.k_left = 5
                    mapNeedsRedraw = True
                    diver.drawCharacterNextImage()
                elif event.key == pygame.K_UP:
                    diver.k_up = 2
                    mapNeedsRedraw = True
                    diver.drawCharacterNextImage()
                elif event.key == pygame.K_DOWN:
                    diver.k_down = -2
                    mapNeedsRedraw = True
                    diver.drawCharacterNextImage()
                elif event.key == pygame.K_ESCAPE: # Esc key quits
                    done = True
            elif event.type == pygame.KEYUP: # to cover when a key is released
                if event.key == pygame.K_RIGHT:
                    diver.k_right = 0
                    mapNeedsRedraw = True
                elif event.key == pygame.K_LEFT:
                    diver.k_left = 0
                    mapNeedsRedraw = True
                elif event.key == pygame.K_UP:
                    diver.k_up = 0
                    mapNeedsRedraw = True
                elif event.key == pygame.K_DOWN:
                    diver.k_down = 0
                    mapNeedsRedraw = True

        # update the camera
        camera -= diver.velocity

        # tick the clock
        time = clock.tick(60) # sets the game to 60FPS
        all_sprites.update(time)

        # draw all the sprites to the screen
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+camera)

        # draw the hud
        drawHealthBar(diver.getHealth())
        drawOxygenBar(diver.getOxygen())

        # finally, update the surface of the screen
        pygame.display.flip()


def main_menu():
    """[ create a main menu]

    """
    # init
    menuOceanDiver = os.path.join(os.path.dirname(full_path), 'Images', 'Menu', 'oceandiver.jpg')

    # start some menu music
    #pygame.mixer.music.load('Sounds/MainMenu.flac')
    #pygame.mixer.music.play(-1, 0.0)

    # create the actions for each menu option
    def menu_new_game():
        """ Start new game option in main menu
        """
        level_menu()
    def menu_load_game():
        """ Load game option in main menu
        """
        pass
    def menu_save_game():
        """ Save game option in main menu
        """
        pass
    def menu_how_to_play():
        """ How to play option in main menu
        """
        pass
    def menu_options():
        """ Options in main menu
        """
        pass
    def menu_high_scores():
        """ Options in main menu
        """
        pass

    # finally, create the actual menu
    main_menu = pygame_menu.Menu(600, 840, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)
    main_menu.add_image(menuOceanDiver, angle=-10, scale=(1.0, 1.0), scale_smooth=True)
    main_menu.add_button('Start New Game', menu_new_game)
    main_menu.add_button('Load Game - TODO', menu_load_game)
    main_menu.add_button('Save Game - TODO', menu_save_game)
    main_menu.add_button('How To Play - TODO', menu_how_to_play)
    main_menu.add_button('Options - TODO', menu_options)
    main_menu.add_button('High Scores - TODO', menu_high_scores)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)
    # display the main menu before anything else
    main_menu.mainloop(screen)


def level_menu():
    """[ create a level menu]

    """

    # init
    full_path = os.path.realpath(__file__)
    path, filename = os.path.split(full_path)
    menuUnderwaterBGBlank = os.path.join(os.path.dirname(full_path), 'Images', 'Menu', 'UnderwaterBGBlank.png')

    # start some menu music
    #pygame.mixer.music.load('Sounds/MainMenu.flac')
    #pygame.mixer.music.play(-1, 0.0)

    # create the actions for each menu option
    def menu_coastal_dive():
        """ Coastal dive  in level menu
        """
        main_loop()
    def menu_coral_reef_dive():
        """ Coral reef dive in level menu
        """
        #pygame.mixer.music.stop()
        pass
    def menu_wreck_dive():
        """ Wreck dive in level menu
        """
        #pygame.mixer.music.stop()
        pass
    def menu_cave_dive():
        """ Cave dive in level menu
        """
        #pygame.mixer.music.stop()
        pass
    def menu_mangrove_dive():
        """ Mangrove dive in level menu
        """
        pass
    def menu_antarctica_dive():
        """ Antarctica dive in level menu
        """
        pygame.mixer.music.stop()

    # finally, create the actual menu
    level_menu = pygame_menu.Menu(600, 840, 'Levels', theme=pygame_menu.themes.THEME_BLUE)
    level_menu.add_image(menuUnderwaterBGBlank, angle=-10, scale=(0.2, 0.2), scale_smooth=True)
    level_menu.add_button('(1) Coastal Dive', menu_coastal_dive)
    level_menu.add_button('(2) Coral Reef Dive - TODO', menu_coral_reef_dive)
    level_menu.add_button('(3) Wreck Dive - TODO', menu_wreck_dive)
    level_menu.add_button('(4) Cave Dive - TODO', menu_cave_dive)
    level_menu.add_button('(5) Mangrove Dive - TODO', menu_mangrove_dive)
    level_menu.add_button('(6) Antarctica Dive - TODO', menu_antarctica_dive)
    level_menu.add_button('Quit', pygame_menu.events.EXIT)
    # display the main menu before anything else
    level_menu.mainloop(screen)


def terminate():
    """ Terminates the game when called

    """
    pygame.quit()
    sys.exit()


def main():
    """ main function

    """
    # run the main game loop
    main_menu()
    level_menu() # main() is run when a level is selected from level_menu
    terminate()


if __name__ == '__main__':
    """ This calls the 'main' function when this script is executed
    """
    main()