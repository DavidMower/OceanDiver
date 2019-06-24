# hud.py
# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0
import pygame
from settings import *
from main import *


# creates a health bar
def drawHealthBar(aPlayerHealth):
    for c in range(aPlayerHealth): # draw the red health bars
        pygame.draw.rect(displaySurf, colourRed, (15, 20 + (10 * player1.getHealth()) - c * 10, 20, 10))
    for m in range(player1.getHealth()):
        pygame.draw.rect(displaySurf, colourBlack, (15, 20 + (10 * player1.getHealth()) - m * 10, 20, 10), 1)
    healthBarSurf, healthBarRect = writeText('H', colourGreen, colourBlue, 5, 5)
    healthBarSurf.blit(healthBarSurf, healthBarRect)


# creates a oxygen bar
def drawOxygenBar(aPlayerHealth):
    for c in range(aPlayerHealth): # draw the blue oxygen bars 
        pygame.draw.rect(displaySurf, colourBlue, (windowWidth - 35, 25 + (10 * player1.getOxygen()) - c * 10, 20, 10))
    for m in range(player1.getOxygen()):
        pygame.draw.rect(displaySurf, colourBlack, (windowWidth - 35, 25 + (10 * player1.getOxygen()) - m * 10, 20, 10), 1)
    oxygenBarSurf, oxygenBarRect = writeText('O', colourGreen, colourBlue, 20, 20)
    oxygenBarSurf.blit(oxygenBarSurf, oxygenBarRect)