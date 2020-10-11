
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
        gameStateObj['player'] = (playerx + xOffset, playery + yOffset)
        return True
    # Check to ensure player stays within the screen
    if level.isEdgeOfScreen(mapObj, playerx + xOffset, playery + yOffset): # if it's the edge of the screen, don't allow the move
        return False
    else:
        gameStateObj['player'] = (playerx + xOffset, playery + yOffset)
        return True