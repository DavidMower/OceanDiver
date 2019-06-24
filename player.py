# player.py
# Scuba Diver
# by David Mower (davidmower84@gmail.com)
# Released under GNU General Public License v3.0 

class Player:
    # class contructer for a 'Player' object
    # a player object contains name, health and oxygen attributes
    def __init__(self, aName, aStartX, aStartY, aHealth, aOxygen):
        self.name = aName
        self.startX = aStartX
        self.startY = aStartY
        self.health = aHealth
        self.oxygen = aOxygen

    # getter method for player's name
    # gets the player's current name value and returns as an string
    def getName(self):
        return self.name

    # setter method for player's name
    # sets the player's name value to argument value (must be a string)
    def setName(self, aName):
       self.name = aName

    # getter method for player's starting X coordinate
    # gets the player's current startX value and returns as an integer
    def getStartX(self):
        return self.startX

    # setter method for player's starting X coordinate
    # sets the player's startX value to argument value (must be an integer)
    def setName(self, aStartX):
       self.startX = aStartX

    # getter method for player's starting Y coordinate
    # gets the player's current startY value and returns as an integer
    def getStartY(self):
        return self.startY

    # setter method for player's starting Y coordinate
    # sets the player's startY value to argument value (must be an integer)
    def setStartY(self, aStartY):
       self.startY = aStartY

    # getter method for player's health
    # gets the player's current health value and returns as an integer
    def getHealth(self):
        return self.health

    # setter method for player's health
    # sets the player's health value to argument value (must be an integer)
    def setHealth(self, aHealth):
       self.health = aHealth

    # getter method for player's oxygen
    # gets the player's current oxygen value and returns as an integer
    def getOxygen(self):
        return self.oxygen

    # setter method for player's oxygen
    # sets the player's oxygen value to argument value (must be an integer)
    def setOxygen(self, aOxygen):
       self.oxygen = aOxygen