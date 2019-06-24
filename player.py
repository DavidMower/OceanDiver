# player.py

# player class for main player's character

class Player:
    # class contructer
    # a player object contains name, health and oxygen attributes
    def __init__(self, aName, aHealth, aOxygen):
        self.name = aName
        self.health = aHealth
        self.oxygen = aOxygen

    # getter method for player's name
    def getName(self):
        return self.name

    # setter method for player's name
    def setName(self, aName):
       self.name = aName

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