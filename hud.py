# hud.py
# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0
import pygame
from settings import *
from main import *

# creates a health bar
# requires an integer value as an argument which the current amount of health
def drawHealthBar(aPlayersHealth):
    for eachHealth in range(aPlayersHealth):
        # draw a red health rectangle for each oxygen value
        pygame.draw.rect(displaySurf, colourRed, (15, 20 + (10 * player1.getHealth()) - eachHealth * 10, 20, 10))
    for eachHealth2 in range(player1.getHealth()):
        # draw a black background rectangle for each oxygen value
        pygame.draw.rect(displaySurf, colourBlack, (15, 20 + (10 * player1.getHealth()) - eachHealth2 * 10, 20, 10), 1)
    # write H above the health bar
    healthBarSurf, healthBarRect = writeText('H', colourGreen, colourBlue, 5, 5)
    healthBarSurf.blit(healthBarSurf, healthBarRect)

# creates a oxygen bar
# requires an integer value as an argument which represents the current amount of oxygen
def drawOxygenBar(aPlayersOxygen):
    for eachOxygen in range(aPlayersOxygen):
        # draw a blue oxygen rectangle for each oxygen value
        pygame.draw.rect(displaySurf, colourBlue, (windowWidth - 35, 25 + (10 * player1.getOxygen()) - eachOxygen * 10, 20, 10))
    for eachOxygen2 in range(player1.getOxygen()):
        # draw a black background rectangle for each oxygen value
        pygame.draw.rect(displaySurf, colourBlack, (windowWidth - 35, 25 + (10 * player1.getOxygen()) - eachOxygen2 * 10, 20, 10), 1)
    # write O above the oxygen bar
    oxygenBarSurf, oxygenBarRect = writeText('O', colourGreen, colourBlue, 20, 20)
    oxygenBarSurf.blit(oxygenBarSurf, oxygenBarRect)

# creates a health bar
# requires an integer value as an argument which the current amount of health
#def drawHealthBar(aPlayersHealth):
#    for eachHealth in range(aPlayersHealth):
#        # draw a red health rectangle for each oxygen value
#        pygame.draw.rect(displaySurf, colourRed, (15, 20 + (10 * aPlayersHealth - eachHealth * 10, 20, 10))
#       # draw a black background rectangle for each oxygen value
#        pygame.draw.rect(displaySurf, colourBlack, (15, 20 + (10 * aPlayersHealth - eachHealth * 10, 20, 10), 1)
#    # write H above the health bar
#    healthBarSurf, healthBarRect = writeText('H', colourGreen, colourBlue, 5, 5)
#    healthBarSurf.blit(healthBarSurf, healthBarRect)