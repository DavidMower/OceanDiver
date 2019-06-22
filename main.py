# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 
import pygame, sys, time
from pygame.locals import *
pygame.init()

# frames per second setting
FPS = 60
assert(FPS <= 0, 'FPS must be a positive integer, for example 30 or 60')
fpsClock = pygame.time.Clock()

# create colours  R    G    B
colourWhite   = (255, 255, 255)
colourGreen   = (  0, 255,   0)
colourBlue    = (  0,   0, 128)

# main loop
def main():
    # create surface object
    windowWidth = 1024
    windowHeight = 768
    displaySurf = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption('Scuba Diver')

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

        # title text
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        textSurfaceObj = fontObj.render('Scuba Diver' , True , colourGreen, colourBlue)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (512, 100)
        displaySurf.blit(textSurfaceObj, textRectObj)

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
                pygame.quit()
                sys.exit()

        # redraw the surface object and wait a clock tick
        pygame.display.update()
        fpsClock.tick(FPS)

main()