#####################################################
##                     main.py                     ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 2.7.18 64-bit             ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import sys, pygame, settings, level
from pygame.locals import *
from player import *
from menus import *
from hud import *


def main():
    """ main function
    """
    print("starting display init")
    pygame.init()
    pygame.display.set_caption('Scuba Diver')
    print("starting showMainMenu")
    showMainMenu()
    print("starting showLevelMenu")
    showLevelMenu()
    while True:
        """ Run the level to play the game.
        If current level has been completed then go to next level until no levels remain.
        """
        print("starting a level")
        levelResult = level.runLevel(settings.levels, settings.currentLevelIndex)
        if levelResult in ('solved', 'next'):
            settings.currentLevelIndex += 1
            if settings.currentLevelIndex >= len(settings.levels):
                settings.currentLevelIndex = 0
        elif levelResult == 'back':
            settings.currentLevelIndex -= 1
            if settings.currentLevelIndex < 0:
                settings.currentLevelIndex = len(settings.levels)-1
        elif levelResult == 'reset':
            pass

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
    textSurf = settings.defaultFont.render(aText, True, aColour, aBackgroundColour)
    textRect = textSurf.get_rect()
    textRect.topleft = (aTop, aLeft)
    return (textSurf, textRect)

def checkForKeyPress():
    """ Waits for any key to be pressed before proceeding
    if key was x to close the window, quit the game
    if no key was pressed, do nothing
    if key was Esc, quit the game
    Returns:
        [type]: [return which key was pressed]
    """
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def terminate():
    """ Terminates the game when called
    """
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    """ Start the main() loop function
    """
    main()