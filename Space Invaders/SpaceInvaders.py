from classes.gameClass import *

# main file for running and ending game

if __name__ == '__main__':
    # creates game object
    SpaceInvaders = Game()

    #calls startGame function
    SpaceInvaders.startGame()

    #quits on end of game
    pygame.quit()

    #exits
    exit()