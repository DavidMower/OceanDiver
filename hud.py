#####################################################
##                     main.py                     ##
##                   Ocean Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##                Python 3.8.2 32-bit              ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import pygame as pg
from settings import *


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
    DEFAULT_FONT = pg.font.Font('freesansbold.ttf', DEFAULT_FONT_SIZE)
    textSurf = DEFAULT_FONT.render(aText, True, aColour, aBackgroundColour)
    textRect = textSurf.get_rect()
    textRect.topleft = (aTop, aLeft)
    return (textSurf, textRect)

def draw_player_health(surf, x , y, health):
    if health < 0:
        health = 0
    fill = health * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if health > 60:
        col = GREEN
    elif health > 30:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

def draw_player_oxygen(surf, x , y, oxygen):
    if oxygen < 0:
        oxygen = 0
    fill = oxygen * BAR_LENGTH
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    if oxygen > 60:
        col = DARKBLUE
    elif oxygen > 30:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)
    writeText('Oxygen', WHITE, BLACK, 18, 5)