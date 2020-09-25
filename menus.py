#####################################################
##                    menus.py                     ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame, settings, main

def showMainMenu():
    """ Create a main menu.
    Fill the screen with a colour to create a background for the menu.
    Start playing main-menu background music.
    Draw the main menu title text.
    Draw the main menu buttons.
    Loop to wait for a key press, so I can test the menu
    """
    while True:
        settings.displaySurf.fill(settings.colourWhite)
        pygame.mixer.music.load('Sounds/MainMenu.flac')
        pygame.mixer.music.play(-1, 0.0)
        mainTitleSurf, mainTitleRect = main.writeText('Scuba Diver', settings.colourGreen, settings.colourBlue, settings.windowWidth - 612, settings.windowHeight - 620)
        settings.displaySurf.blit(mainTitleSurf, mainTitleRect)
        newGameSurf, newGameRect       = main.writeText('Start New Game', settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 520)
        settings.displaySurf.blit(newGameSurf, newGameRect)
        loadGameSurf, loadGameRect     = main.writeText(  'Load Game',    settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 470)
        settings.displaySurf.blit(loadGameSurf, loadGameRect)
        saveGameSurf, saveGameRect     = main.writeText(  'Save Game',    settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 420)
        settings.displaySurf.blit(saveGameSurf, saveGameRect)
        howToPlaySurf, howToPlayRect   = main.writeText( 'How to Play',   settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 370)
        settings.displaySurf.blit(howToPlaySurf, howToPlayRect)
        optionsSurf, optionsRect       = main.writeText(   'Options',     settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 320)
        settings.displaySurf.blit(optionsSurf, optionsRect)
        highScoresSurf, highScoresRect = main.writeText( 'High Scores',   settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 270)
        settings.displaySurf.blit(highScoresSurf, highScoresRect)
        quitSurf, quitRect             = main.writeText(    'Quit',       settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 220)
        settings.displaySurf.blit(quitSurf, quitRect)
        if main.checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update() # draw these objects on the display
        settings.FPSClock.tick(settings.FPS) # process to next clock tick


def showLevelMenu():
    """ Create level selection menu.
    Fill the screen with a colour to create a background for the menu.
    Draw the level menu title text.
    Draw the level menu buttons.
    Loop to wait for a key press, so I can test the menu.
    """
    while True:
        settings.displaySurf.fill(settings.colourWhite)
        levelMenuTitleSurf, levelMenuTitleRect = main.writeText('Level select', settings.colourGreen, settings.colourBlue, settings.windowWidth - 612, settings.windowHeight - 620)
        settings.displaySurf.blit(levelMenuTitleSurf, levelMenuTitleRect)
        menuCoastalSurf, menuCoastalRect       = main.writeText('  (1) Coastal Dive',   settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 520)
        settings.displaySurf.blit(menuCoastalSurf, menuCoastalRect)
        menuCoralReefSurf, menuCoralReefRect   = main.writeText(' (2) Coral Reef Dive', settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 470)
        settings.displaySurf.blit(menuCoralReefSurf, menuCoralReefRect)
        menuWreckSurf, menuWreckRect           = main.writeText('   (3) Wreck Dive',    settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 420)
        settings.displaySurf.blit(menuWreckSurf, menuWreckRect)
        menuCaveSurf, menuCaveRect             = main.writeText('   (4) Cave Dive',     settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 370)
        settings.displaySurf.blit(menuCaveSurf, menuCaveRect)
        menuMangroveSurf, menuMangroveRect     = main.writeText('  (5) Mangrove Dive',  settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 320)
        settings.displaySurf.blit(menuMangroveSurf, menuMangroveRect)
        menuAntarcticaSurf, menuAntarcticaRect = main.writeText( '(6) Antarctica Dive', settings.colourBlack, settings.colourWhite, settings.windowWidth - 612, settings.windowHeight - 270)
        settings.displaySurf.blit(menuAntarcticaSurf, menuAntarcticaRect)
        if main.checkForKeyPress():
            pygame.event.get() # clear event queue
            pygame.mixer.music.stop() # stop the main menu background music
            return
        pygame.display.update() # draw these objects on the display
        settings.FPSClock.tick(settings.FPS) # process to next clock tick