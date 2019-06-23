# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 
import pygame, sys, time
from pygame.locals import *

# Init
FPS = 60 # frames per second setting
assert(FPS <= 0, 'FPS must be a positive integer, for example 30 or 60')
defaultFontSize = 32 # default font size for text

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

# main loop
def main():
    global displaySurf, fpsClock, defaultFont, windowHeight, windowWidth
    # create surface object
    pygame.init()
    fpsClock = pygame.time.Clock()
    windowWidth = 1024
    windowHeight = 768
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Scuba Diver')
    defaultFont = pygame.font.Font('freesansbold.ttf', defaultFontSize)

    showMainMenu()
    while True:
        runGameLoop()

# main menu loop
def showMainMenu():
    global newGameSurf, newGameRect, loadGameSurf, loadGameRect, saveGameSurf, saveGameRect, howToPlaySurf, howToPlayRect, optionsSurf, optionsRect, highScoresSurf, highScoresRect, quitSurf, quitRect

    while True:
        displaySurf.fill(colourWhite)

        # start playing main-menu music
        pygame.mixer.music.load('Sounds/MainMenu.flac')
        pygame.mixer.music.play(-1, 0.0)

        # draw the main menu title text
        titleSurf, titleRect = writeText('Scuba Diver', colourGreen, colourBlue, windowWidth - 612, windowHeight - 620)
        displaySurf.blit(titleSurf, titleRect)

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
            pygame.event.get() # clear event queue
            pygame.mixer.music.stop() # stop the main menu background music
            return
        pygame.display.update()
        fpsClock.tick(FPS)

# main in-game loop
def runGameLoop():
    # create the scuba diver character
    diverImg = pygame.image.load('Images/ScubaDiver.png')
    diverx = 310
    divery = 310
    direction = 'right'

    # start playing CoastalDive background music
    pygame.mixer.music.load('Sounds/CoastalDive.flac')
    pygame.mixer.music.play(-1, 0.0)

    while True:
        displaySurf.fill(colourWhite)

        # test sound effect
        #soundObj = pygame.mixer.Sound('Sounds/beeps.wav')
        #soundObj.play()
        #time.sleep(1) # let the sound play for 1 second
        #soundObj.stop()

        # loops to keep diver on the move
        if direction == 'right':
            diverx += 5
            if diverx == 725:
                direction = 'down'
        elif direction == 'down':
            divery += 5
            if divery == 470:
                direction = 'left'
        elif direction == 'left':
            diverx -= 5
            if diverx == 300:
                direction = 'up'
        elif direction == 'up':
            divery -= 5
            if divery == 300:
                direction = 'right'

        # copy diverImg to displaySurf with coordinates
        displaySurf.blit(diverImg, (diverx, divery))

        for event in pygame.event.get():
            # if event is quit by closing the window or pressing esc, terminate the program
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.mixer.music.stop()
                terminate()

        # redraw the surface object and wait a clock tick
        pygame.display.update()
        fpsClock.tick(FPS)

# start the main() loop function
main()