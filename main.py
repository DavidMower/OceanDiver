#####################################################
##                     main.py                     ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 2.7.18 64-bit             ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import sys, pygame, pygame_menu
import settings, level
from pygame.locals import *
from player import *
from hud import *


def main():
    """ main function
    """
    print("starting display init")
    pygame.init()
    pygame.display.set_caption('Scuba Diver')
    # create the level menu
    pygame.mixer.music.load('Sounds/MainMenu.flac')
    pygame.mixer.music.play(-1, 0.0)
    def menu_coastal_dive():
        """ Coastal dive  in level menu
        """
        pygame.mixer.music.stop()
        while True:
            """ Run the level to play the game.
            If current level has been completed then go to next level until no levels remain.
            """
            pygame.display.update() # draw these objects on the display
            settings.FPSClock.tick(settings.FPS) # process to next clock tick

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
    def menu_coral_reef_dive():
        """ Coral reef dive in level menu
        """
        pygame.mixer.music.stop()
    def menu_wreck_dive():
        """ Wreck dive in level menu
        """
        pygame.mixer.music.stop()
    def menu_cave_dive():
        """ Cave dive in level menu
        """
        pygame.mixer.music.stop()
    def menu_mangrove_dive():
        """ Mangrove dive in level menu
        """
        pass
    def menu_antarctica_dive():
        """ Antarctica dive in level menu
        """
        pygame.mixer.music.stop()
    level_menu = pygame_menu.Menu(600, 840, 'Levels', theme=pygame_menu.themes.THEME_BLUE)
    level_menu.add_image(settings.menuUnderwaterBGBlank, angle=-10, scale=(0.2, 0.2), scale_smooth=True)
    level_menu.add_button('(1) Coastal Dive', menu_coastal_dive)
    level_menu.add_button('(2) Coral Reef Dive - TODO', menu_coral_reef_dive)
    level_menu.add_button('(3) Wreck Dive - TODO', menu_wreck_dive)
    level_menu.add_button('(4) Cave Dive - TODO', menu_cave_dive)
    level_menu.add_button('(5) Mangrove Dive - TODO', menu_mangrove_dive)
    level_menu.add_button('(6) Antarctica Dive - TODO', menu_antarctica_dive)
    level_menu.add_button('Quit', pygame_menu.events.EXIT)
    # create the main menu
    pygame.mixer.music.load('Sounds/MainMenu.flac')
    pygame.mixer.music.play(-1, 0.0)
    def menu_new_game():
        """ Start new game option in main menu
        """
        level_menu.mainloop(settings.displaySurf)
    def menu_load_game():
        """ Load game option in main menu
        """
        pass
    def menu_save_game():
        """ Save game option in main menu
        """
        pass
    def menu_how_to_play():
        """ How to play option in main menu
        """
        pass
    def menu_options():
        """ Options in main menu
        """
        pass
    def menu_high_scores():
        """ Options in main menu
        """
        pass
    main_menu = pygame_menu.Menu(600, 840, 'Welcome', theme=pygame_menu.themes.THEME_BLUE)
    main_menu.add_image(settings.menuOceanDiver, angle=-10, scale=(1.0, 1.0), scale_smooth=True)
    main_menu.add_button('Start New Game', menu_new_game)
    main_menu.add_button('Load Game - TODO', menu_load_game)
    main_menu.add_button('Save Game - TODO', menu_save_game)
    main_menu.add_button('How To Play - TODO', menu_how_to_play)
    main_menu.add_button('Options - TODO', menu_options)
    main_menu.add_button('High Scores - TODO', menu_high_scores)
    main_menu.add_button('Quit', pygame_menu.events.EXIT)
    # display the main menu before anything else
    main_menu.mainloop(settings.displaySurf)

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