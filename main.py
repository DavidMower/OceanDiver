import pygame, sys
from pygame.locals import *
pygame.init()

# Frames per second setting
FPS = 60
fpsClock = pygame.time.Clock()

# Create surface object
DISPLAYSURF = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Ocean Diver')

# Create the colours
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

# Create the scuba diver character
diverImg = pygame.image.load('Images/ScubaDiver.png')
diverx = 310
divery = 310
direction = 'right'

# Main loop
while True:
    DISPLAYSURF.fill(WHITE)

    # Title Text
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Scuba Diver' , True, GREEN, BLUE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (512, 100)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    # Loops to keep diver on the move
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

    # Copy diverImg to DISPLAYSURF with coordinates
    DISPLAYSURF.blit(diverImg, (diverx, divery))

    for event in pygame.event.get():
        # If event is quit, terminate the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Draw the surface object
    pygame.display.update()
    fpsClock.tick(FPS)