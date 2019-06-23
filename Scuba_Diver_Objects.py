import pygame, mainloop
from pygame.locals import *

def main():
    global environementImages, environementMapping, outsideDecoMapping, characterImages, currentImage

    # A global dictionary that'll contain all the Pygame Surface objects
    environementImages = {'uncovered goal': pygame.image.load('RedSelector.png'),
                          'covered goal': pygame.image.load('Selector.png'),
                          'star': pygame.image.load('Star.png'),
                          'corner': pygame.image.load('Images/Dark_Rock_Block.png'),
                          'wall': pygame.image.load('Images/Rock_Block.png'),
                          'inside floor': pygame.image.load('Images/Sand_Block.png'),
                          'outside floor': pygame.image.load('Images/Ocean_Block.png'),
                          'title': pygame.image.load('star_title.png'),
                          'solved': pygame.image.load('star_solved.png'),
                          'princess': pygame.image.load('Images/Scuba_Diver.png'),
                          'boy': pygame.image.load('boy.png'),
                          'catgirl': pygame.image.load('catgirl.png'),
                          'horngirl': pygame.image.load('horngirl.png'),
                          'pinkgirl': pygame.image.load('pinkgirl.png'),
                          'rock': pygame.image.load('Rock.png'),
                          'short tree': pygame.image.load('Tree_Short.png'),
                          'tall tree': pygame.image.load('Tree_Tall.png'),
                          'ugly tree': pygame.image.load('Tree_Ugly.png')}

    # These dictionary values are global, and map the character that appear in the level file
    environementMapping = {'x': environementImages['corner'],
                           '#': environementImages['wall'],
                           'o': environementImages['inside floor'],
                           ' ': environementImages['outside floor']}
    outsideDecoMapping = { '1': environementImages['rock'],
                           '2': environementImages['short tree'],
                           '3': environementImages['tall tree'],
                           '4': environementImages['ugly tree']}
                           
    # characterImages is a list of all possible characters the player can be.
    # currentImage is the index of the player's current player image.
    currentImage = 0
    characterImages = [environementImages['princess'],
                       environementImages['boy'],
                       environementImages['catgirl'],
                       environementImages['horngirl'],
                       environementImages['pinkgirl']]

# start the main() loop function
if __name__ == '__main__':
    main()