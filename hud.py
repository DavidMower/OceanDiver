#####################################################
##                     hud.py                      ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame, main, settings


def drawHealthBar(aPlayersHealth):
    """ Creates a health bar

    Args:
        aPlayersHealth ([int]): [current amount of health]
    """
    for eachHealth in range(aPlayersHealth):
        # draw a red health rectangle for each oxygen value
        pygame.draw.rect(settings.displaySurf, settings.colourRed, (15, 20 + (10 * settings.player1.getHealth()) - eachHealth * 10, 20, 10))
    for eachHealth2 in range(settings.player1.getHealth()):
        # draw a black background rectangle for each oxygen value
        pygame.draw.rect(settings.displaySurf, settings.colourBlack, (15, 20 + (10 * settings.player1.getHealth()) - eachHealth2 * 10, 20, 10), 1)
    # write H above the health bar
    healthBarSurf, healthBarRect = main.writeText('H', settings.colourGreen, settings.colourBlue, 5, 5)
    healthBarSurf.blit(healthBarSurf, healthBarRect)

def drawOxygenBar(aPlayersOxygen):
    """ Creates a oxygen bar.
    Draw a blue oxygen rectangle for each oxygen value.
    Draw a black background rectangle for each oxygen value.
    Print an O above the oxygen bar.

    Args:
        aPlayersOxygen ([int]): [current amount of oxygen]
    """
    for eachOxygen in range(aPlayersOxygen):
        pygame.draw.rect(settings.displaySurf, settings.colourBlue,  (settings.windowWidth - 35, 25 + (10 * settings.player1.getOxygen()) - eachOxygen * 10, 20, 10))
    for eachOxygen2 in range(settings.player1.getOxygen()):
        pygame.draw.rect(settings.displaySurf, settings.colourBlack, (settings.windowWidth - 35, 25 + (10 * settings.player1.getOxygen()) - eachOxygen2 * 10, 20, 10), 1)
    oxygenBarSurf, oxygenBarRect = main.writeText('O', settings.colourGreen, settings.colourBlue, 20, 20)
    oxygenBarSurf.blit(oxygenBarSurf, oxygenBarRect)

#def drawHealthBar(aPlayersHealth):
    """ Creates a health bar
    Draw a red health rectangle for each oxygen value.
    Draw a black background rectangle for each oxygen value.
    Write H above the health bar.

    Args:
        aPlayersHealth ([int]): [current amount of health]
    """
#    for eachHealth in range(aPlayersHealth):
#        pygame.draw.rect(displaySurf, colourRed,   (15, 20 + (10 * aPlayersHealth - eachHealth * 10, 20, 10))
#        pygame.draw.rect(displaySurf, colourBlack, (15, 20 + (10 * aPlayersHealth - eachHealth * 10, 20, 10), 1)
#    healthBarSurf, healthBarRect = writeText('H', colourGreen, colourBlue, 5, 5)
#    healthBarSurf.blit(healthBarSurf, healthBarRect)
