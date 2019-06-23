# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 
import pygame, sys, time
from pygame.locals import *

# Initialisations
FPS = 60 # frames per second setting
assert(FPS <= 0, 'FPS must be a positive integer, for example 30 or 60')
defaultFontSize = 32 # default font size for text
UP = 'up' # shorthand for up
DOWN = 'down' # shorthand for down
LEFT = 'left' # shorthand for left
RIGHT = 'right' # shorthand for right
moveFrequency = 0.15 # threshold to trigger key held down status
maxHealthDiver = 75 # how much health the player starts with
maxOxygenDiver = 75 # how much oxygen the player starts with

# create the colours  R    G    B
colourBlack       = (  0,   0,   0)
colourBlue        = (  0,   0, 128)
colourGreen       = (  0, 255,   0)
colourRed         = (155,   0,   0)
colourWhite       = (255, 255, 255)
colourYellow      = (155, 155,   0)

# terminates the game when called
def terminate():
    pygame.quit()
    sys.exit()
    
# creates the Surface and Rect objects for some text
def writeText(aText, aColour, aBackgroundColour, aTop, aLeft):
    textSurf = defaultFont.render(aText, True, aColour, aBackgroundColour)
    textRect = textSurf.get_rect()
    textRect.topleft = (aTop, aLeft)
    return (textSurf, textRect)

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

# creates the scuba diver character
def makeNewDiver():
    global playerObj, diverCoords
    playerObj = {'diverImg': pygame.image.load('Images/ScubaDiver.png'),
                'diverX': 560,
                'diverY': 380,
                'health': maxHealthDiver,
                'oxygen': maxOxygenDiver
                }
    direction = RIGHT
    diverCoords = {'x': playerObj['diverX'], 'y': playerObj['diverY']} # a dictionary to hold the divers current position

# creates a health bar
def drawHealthBar(currentDiverHealth):
    for c in range(currentDiverHealth): # draw the red health bars
        pygame.draw.rect(displaySurf, colourRed, (5, 20 + (10 * maxHealthDiver) - c * 10, 20, 10))
    for m in range(maxHealthDiver):
        pygame.draw.rect(displaySurf, colourBlack, (5, 20 + (10 * maxHealthDiver) - m * 10, 20, 10), 1)
    healthBarSurf, healthBarRect = writeText('Hasdasdassfsdfsdfsfasdfasdf', colourGreen, colourBlue, 5, 5)
    healthBarSurf.blit(healthBarSurf, healthBarRect)

# creates a oxygen bar
def drawOxygenBar(currentDiverOxygen):
    for c in range(currentDiverOxygen): # draw the blue oxygen bars 
        pygame.draw.rect(displaySurf, colourBlue, (30, 20 + (10 * maxOxygenDiver) - c * 10, 20, 10))
    for m in range(maxOxygenDiver):
        pygame.draw.rect(displaySurf, colourBlack, (30, 20 + (10 * maxOxygenDiver) - m * 10, 20, 10), 1)
    oxygenBarSurf, oxygenBarRect = writeText('Osfasdgdfhgddfghfhfgfgh', colourGreen, colourBlue, 20, 20)
    oxygenBarSurf.blit(oxygenBarSurf, oxygenBarRect)

# main loop
def main():
    global displaySurf, fpsClock, defaultFont, windowHeight, windowWidth
    # create surface object
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowWidth = 1200
    windowHeight = 800
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Scuba Diver')
    defaultFont = pygame.font.Font('freesansbold.ttf', defaultFontSize)

    # launch the main menu
    showMainMenu()
    while True:
        runGameLoop()
        showGameOver()

# main menu loop
def showMainMenu():
    global newGameSurf, newGameRect, loadGameSurf, loadGameRect, saveGameSurf, saveGameRect, howToPlaySurf, howToPlayRect, optionsSurf, optionsRect, highScoresSurf, highScoresRect, quitSurf, quitRect

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
        fpsClock.tick(FPS)

# level menu loop
def showLevelMenu():
    global menuCoastalSurf, menuCoastalRect, menuCoralReefSurf, menuCoralReefRect, menuWreckSurf, menuWreckRect, menuCaveSurf, menuCaveRect, menuMangroveSurf, menuMangroveRect, menuAntarcticaSurf, menuAntarcticaRect

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
        fpsClock.tick(FPS)

# main in-game loop
def runGameLoop():
    # create a new scuba diver
    makeNewDiver()
    newDiverX = None
    newDiverY = None

    # start playing CoastalDive background music
    pygame.mixer.music.load('Sounds/CoastalDive.flac')
    pygame.mixer.music.play(-1, 0.0)

    while True:
        displaySurf.fill(colourWhite)

        # draw the player health and oxygen bars
        drawHealthBar(playerObj['health'])
        drawOxygenBar(playerObj['oxygen'])

        # test sound effect
        #soundObj = pygame.mixer.Sound('Sounds/beeps.wav')
        #soundObj.play()
        #time.sleep(1) # let the sound play for 1 second
        #soundObj.stop()

        for event in pygame.event.get():
            # if event is quit by closing the window or pressing esc, terminate the program
            if event.type == QUIT:
                pygame.mixer.music.stop()
                terminate()
            # update direction of diver if correct key is pressed
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a): # and ((time.time() - lastMoveTime) > moveFrequency): PAGE 179
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d):
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w):
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s):
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

            # move the diver in the correct direction
            if event.type == KEYDOWN:
                if direction == UP and not diverCoords['y'] == 0: # checks if top of screen has been hit
                    newDiverY = diverCoords.get('y') - 10
                elif direction == DOWN and not diverCoords['y'] == (windowHeight - 60): # checks if bottom of screen has been hit
                    newDiverY = diverCoords.get('y') + 10
                elif direction == LEFT and not diverCoords['x'] == 0: # checks if left of screen has been hit
                    newDiverX = diverCoords.get('x') - 10
                elif direction == RIGHT and not diverCoords['x'] == (windowWidth - 50): # checks if right of screen has been hit
                    newDiverX = diverCoords.get('x') + 10      
                if newDiverX is not None:
                    diverCoords['x'] = newDiverX
                if newDiverY is not None:
                    diverCoords['y'] = newDiverY

        # copy diverImg to displaySurf with coordinates
        displaySurf.blit(playerObj['diverImg'], (diverCoords['x'], diverCoords['y']))

        # reset the diver movement variable
        newDiverX is None
        newDiverY is None

        # redraw the surface object and wait a clock tick
        pygame.display.update()
        fpsClock.tick(FPS)

def showGameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, colourWhite)
    gameRect = gameSurf.get_rect()
    overSurf = gameOverFont.render('Over', True, colourWhite)
    overRect = overSurf.get_rect()
    gameRect.midtop = (screenWidth / 2, 10)
    overRect.midtop = (screenWidth / 2, gameRect.height + 10 + 25)

    displaySurf.blit(gameSurf, gameRect)
    displaySurf.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

# start the main() loop function
if __name__ == '__main__':
    main()