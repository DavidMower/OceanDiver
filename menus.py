# menus.py
# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0
import pygame
from settings import *
from main import *


# main menu loop
def showMainMenu():
    while True:
        displaySurf.fill(colourWhite)

        # start playing main-menu music
        pygame.mixer.music.load('Sounds/MainMenu.flac')
        pygame.mixer.music.play(-1, 0.0)

        # draw the main menu title text
        mainTitleSurf, mainTitleRect = writeText('Scuba Diver', colourGreen, colourBlue, windowWidth - 612, windowHeight - 620)
        displaySurf.blit(mainTitleSurf, mainTitleRect)

        # draw the main menu buttons
        newGameSurf, newGameRect       = writeText('Start New Game', colourBlack, colourWhite, windowWidth - 612, windowHeight - 520)
        displaySurf.blit(newGameSurf, newGameRect)
        loadGameSurf, loadGameRect     = writeText(  'Load Game',    colourBlack, colourWhite, windowWidth - 612, windowHeight - 470)
        displaySurf.blit(loadGameSurf, loadGameRect)
        saveGameSurf, saveGameRect     = writeText(  'Save Game',    colourBlack, colourWhite, windowWidth - 612, windowHeight - 420)
        displaySurf.blit(saveGameSurf, saveGameRect)
        howToPlaySurf, howToPlayRect   = writeText( 'How to Play',   colourBlack, colourWhite, windowWidth - 612, windowHeight - 370)
        displaySurf.blit(howToPlaySurf, howToPlayRect)
        optionsSurf, optionsRect       = writeText(   'Options',     colourBlack, colourWhite, windowWidth - 612, windowHeight - 320)
        displaySurf.blit(optionsSurf, optionsRect)
        highScoresSurf, highScoresRect = writeText( 'High Scores',   colourBlack, colourWhite, windowWidth - 612, windowHeight - 270)
        displaySurf.blit(highScoresSurf, highScoresRect)
        quitSurf, quitRect             = writeText(    'Quit',       colourBlack, colourWhite, windowWidth - 612, windowHeight - 220)
        displaySurf.blit(quitSurf, quitRect)

        # temp loop so I can test the menu
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

        pygame.display.update()
        FPSClock.tick(FPS)


# level menu loop
def showLevelMenu():
    while True:
        displaySurf.fill(colourWhite)

        # draw the level menu title text
        levelMenuTitleSurf, levelMenuTitleRect = writeText('Level select', colourGreen, colourBlue, windowWidth - 612, windowHeight - 620)
        displaySurf.blit(levelMenuTitleSurf, levelMenuTitleRect)

        # draw the level menu buttons
        menuCoastalSurf, menuCoastalRect       = writeText('  (1) Coastal Dive',   colourBlack, colourWhite, windowWidth - 612, windowHeight - 520)
        displaySurf.blit(menuCoastalSurf, menuCoastalRect)
        menuCoralReefSurf, menuCoralReefRect   = writeText(' (2) Coral Reef Dive', colourBlack, colourWhite, windowWidth - 612, windowHeight - 470)
        displaySurf.blit(menuCoralReefSurf, menuCoralReefRect)
        menuWreckSurf, menuWreckRect           = writeText('   (3) Wreck Dive',    colourBlack, colourWhite, windowWidth - 612, windowHeight - 420)
        displaySurf.blit(menuWreckSurf, menuWreckRect)
        menuCaveSurf, menuCaveRect             = writeText('   (4) Cave Dive',     colourBlack, colourWhite, windowWidth - 612, windowHeight - 370)
        displaySurf.blit(menuCaveSurf, menuCaveRect)
        menuMangroveSurf, menuMangroveRect     = writeText('  (5) Mangrove Dive',  colourBlack, colourWhite, windowWidth - 612, windowHeight - 320)
        displaySurf.blit(menuMangroveSurf, menuMangroveRect)
        menuAntarcticaSurf, menuAntarcticaRect = writeText( '(6) Antarctica Dive', colourBlack, colourWhite, windowWidth - 612, windowHeight - 270)
        displaySurf.blit(menuAntarcticaSurf, menuAntarcticaRect)

        # temp loop so I can test the menu
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            pygame.mixer.music.stop() # stop the main menu background music
            return
            
        pygame.display.update()
        FPSClock.tick(FPS)