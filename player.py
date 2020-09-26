#####################################################
##                    player.py                    ##
##                   Scuba Diver                   ##
##     by David Mower (davidmower84@gmail.com)     ##
##  Released under GNU General Public License v3.0 ##
#####################################################

import level, settings

class Player:
    """ Player class for the main character.

    Returns:
        [type]: [description]
    """

    def __init__(self, aName, aStartX, aStartY, aHealth, aOxygen):
        """ Class contructer
        A player object must contain a name, startx, starty, health and oxygen attributes.

        Args:
            aName ([string]): [player character name]
            aStartX ([int]): [coordinate value for starting position from left]
            aStartY ([int]): [coordinate value for starting position from top]
            aHealth ([int]): [players starting health]
            aOxygen ([int]): [players starting oxygen]
        """
        self.name = aName
        self.startX = aStartX
        self.startY = aStartY
        self.health = aHealth
        self.oxygen = aOxygen

    def getName(self):
        """ getter method for player's name

        Returns:
            [string]: [player's current name]
        """
        return self.name

    def setName(self, aName):
        """ setter method for player's name

        Args:
            aName ([string]): [player's new name value]
        """
        self.name = aName

    def getStartX(self):
        """ Getter method for player's starting X coordinate

        Returns:
            [int]: [player's current startX value]
        """
        return self.startX

    def setStartX(self, aStartX):
        """ Setter method for player's starting X coordinate

        Args:
            aStartX ([int]): [player's new startX value]
        """
        self.startX = aStartX

    def getStartY(self):
        """[Getter method for player's starting Y coordinate]

        Returns:
            [int]: [player's current startY value]
        """
        return self.startY

    def setStartY(self, aStartY):
        """[Setter method for player's starting Y coordinate]

        Args:
            aStartY ([type]): [description]
        """
        self.startY = aStartY

    def getHealth(self):
        """ Getter method for player's health

        Returns:
            [int]: [player's current health value]
        """
        return self.health

    def setHealth(self, aHealth):
        """ Setter method for player's health

        Args:
            aHealth ([type]): [player's new health value]
        """
        self.health = aHealth

    def getOxygen(self):
        """[Getter method for player's oxygen]

        Returns:
            [int]: [player's current oxygen value]
        """
        return self.oxygen

    def setOxygen(self, aOxygen):
        """Setter method for player's oxygen

        Args:
            aOxygen ([int]): [player's new oxygen value]
        """
        self.oxygen = aOxygen


# move player if possible
def makeMove(mapObj, gameStateObj, playerMoveTo):
    """ Check if it is possible for the player to move.
    If yes, then change the player's position. If not, do nothing.

    Args:
        mapObj ([mapObj]): [map object]
        gameStateObj ([gameStateObj]): [game state object]
        playerMoveTo ([type]): [description]

    Returns:
        [boolean]: [Returns True if the player moved, otherwise False.]
    """
    playerx, playery = gameStateObj['player']
    # The code for handling each of the directions. Simplified by using the xOffset and yOffset variables.
    if playerMoveTo == settings.UP:
        xOffset = 0
        yOffset = -1
    elif playerMoveTo == settings.RIGHT:
        xOffset = 1
        yOffset = 0
    elif playerMoveTo == settings.DOWN:
        xOffset = 0
        yOffset = 1
    elif playerMoveTo == settings.LEFT:
        xOffset = -1
        yOffset = 0
    # Check if player is trying to move into a wall block
    if level.isWall(mapObj, playerx + xOffset, playery + yOffset): # if it's a wall, don't allow the move
        return False
    else:
        gameStateObj['player'] = (playerx + xOffset, playery + yOffset) # If not a wall, allow the move
        return True