from initializeGame import *
from classes.invaderClass import Invaders

# defineing the MysteryShip Class
class MysteryShip(pygame.sprite.Sprite):
    mysteryScores = [50,100,150,300]
    SPEED = THE_MYSTERY_SHIP_SPEED

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inherits from the pygame.sprite.Sprite class
        self.image = MYSTERY_SHIP  # sets image as the MYSTERYSHIP Text renderer
        self.rect = self.image.get_rect()  # sets rect as rect of the image
        self.rect.centerx = SCREEN_WIDTH / 2  # sets initial centerx
        self.rect.y = 100  # sets height from top
        self.mysteryScore = random.choice(MysteryShip.mysteryScores)         # randomly decides mystery ship score
        MYSTERY_SHIP_SPRITE.add(self)         # adds self to pertinent sprite group

    # updater function left-right oscillation
    def update(self):
        ObjOsc(self)

# creates Mystery Ship
mysteryShip = MysteryShip()
