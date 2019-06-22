# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 
import pygame, sys, time
from pygame.locals import *

# Initialisations
FPS = 60 # frames per second setting
assert(FPS <= 0, 'FPS must be a positive integer, for example 30 or 60')
defaultFontSize = 32

# create colours  R    G    B
colourBlack   = (  0,   0,   0)
colourBlue    = (  0,   0, 128)
colourGreen   = (  0, 255,   0)
colourRed     = (155,   0,   0)
colourWhite   = (255, 255, 255)
colourYellow  = (155, 155,   0)

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

def runGameLoop():
    # create the scuba diver character
    diverImg = pygame.image.load('Images/ScubaDiver.png')
    diverx = 310
    divery = 310
    direction = 'right'

    # start playing background music
    pygame.mixer.music.load('Sounds/backgroundmusic.flac')
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

def showMainMenu():
    global newGameSurf, newGameRect, loadGameSurf, loadGameRect, saveGameSurf, saveGameRect, howToPlaySurf, howToPlayRect, optionsSurf, optionsRect, highScoresSurf, highScoresRect, quitSurf, quitRect
    
    while True:
        displaySurf.fill(colourWhite)

        # main menu title text
        titleFont = defaultFont.render('Scuba Diver' , True , colourGreen, colourBlue)
        textRectObj = titleFont.get_rect()
        textRectObj.center = (512, 150)
        displaySurf.blit(titleFont, textRectObj)

        # store the main menu buttons and their rectangles
        newGameSurf, newGameRect       = makeText('Start New Game', colourBlack, colourWhite, windowWidth - 612, windowHeight - 520)
        loadGameSurf, loadGameRect     = makeText('Load Game', colourBlack, colourWhite, windowWidth - 612, windowHeight - 470)
        saveGameSurf, saveGameRect     = makeText('Save Game', colourBlack, colourWhite, windowWidth - 612, windowHeight - 420)
        howToPlaySurf, howToPlayRect   = makeText('How to Play', colourBlack, colourWhite, windowWidth - 612, windowHeight - 370)
        optionsSurf, optionsRect       = makeText('Options', colourBlack, colourWhite, windowWidth - 612, windowHeight - 320)
        highScoresSurf, highScoresRect = makeText('High Scores', colourBlack, colourWhite, windowWidth - 612, windowHeight - 270)
        quitSurf, quitRect             = makeText('Quit', colourBlack, colourWhite, windowWidth - 612, windowHeight - 220)

        # draw the main menu buttons
        displaySurf.blit(newGameSurf, newGameRect)
        displaySurf.blit(loadGameSurf, loadGameRect)
        displaySurf.blit(saveGameSurf, saveGameRect)
        displaySurf.blit(howToPlaySurf, howToPlayRect)
        displaySurf.blit(optionsSurf, optionsRect)
        displaySurf.blit(highScoresSurf, highScoresRect)
        displaySurf.blit(quitSurf, quitRect)

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        fpsClock.tick(FPS)

# terminates the game when called
def terminate():
    pygame.quit()
    sys.exit()

def makeText(text, color, bgcolor, top, left):
    # create the Surface and Rect objects for some text.
    textSurf = defaultFont.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.topleft = (top, left)
    return (textSurf, textRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

main()