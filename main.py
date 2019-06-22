import pygame, sys
from pygame.locals import *
pygame.init()

# Frames per second setting
FPS = 30
fpsClock = pygame.time.Clock()

# Create surface object
DISPLAYSURF = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Ocean Diver')

WHITE = (255, 255, 255)
catImg = pygame.image.load('Images/ScubaDiver.png')
catx = 10
caty = 10
direction = 'right'

# Main loop
while True:
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'

    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'

    elif direction == 'up':
        caty -=5
        if caty == 10:
            direction = 'right'

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        # If event is quit, terminate the program
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Draw the surface object
    pygame.display.update()
    fpsClock.tick(FPS)