# main.py
# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 
import sys, pygame
from pygame.locals import *
from settings import *
from player import *
from menus import *
from hud import *
from level import *

def main():
    # pygame initialisation
    pygame.init()
    pygame.display.set_caption('Scuba Diver')
    
    # show the menus
    showMainMenu()
    showLevelMenu()

    # The main game loop. This loop runs a single level, when the user finishes that level, the next/previous level is loaded
    while True:
        # Run the level to actually start playing the game:
        levelResult = runLevel(levels, currentLevelIndex)
        # check if this level has already been completed
        if levelResult in ('solved', 'next'):
            # Go to the next level.
            currentLevelIndex += 1
            # If there are no more levels, go back to the first one
            if currentLevelIndex >= len(levels):
                currentLevelIndex = 0
        # check if going back a level
        elif levelResult == 'back':
            # Go to the previous level.
            currentLevelIndex -= 1
            if currentLevelIndex < 0:
                # If there are no previous levels, go to the last one
                currentLevelIndex = len(levels)-1
        elif levelResult == 'reset':
            pass # Do nothing. Loop re-calls runLevel() to reset the level
        

# creates the Surface and Rect objects to write some text
def writeText(aText, aColour, aBackgroundColour, aTop, aLeft):
    textSurf = defaultFont.render(aText, True, aColour, aBackgroundColour)
    textRect = textSurf.get_rect()
    textRect.topleft = (aTop, aLeft)
    return (textSurf, textRect)
        
# waits for any key to be pressed before proceeding
# return which key was pressed
def checkForKeyPress():
    # if key was x to close the window, quit the game
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    # if no key was pressed, do nothing
    if len(keyUpEvents) == 0:
        return None
    # if key was Esc, quit the game
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

# terminates the game when called
def terminate():
    pygame.quit()
    sys.exit()

# start the main() loop function
if __name__ == '__main__':
    main()