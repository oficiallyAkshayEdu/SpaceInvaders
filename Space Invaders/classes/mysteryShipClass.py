from initializeGame import *
from classes.invaderClass import Invaders

class MysteryShip(pygame.sprite.Sprite):
    mysteryScores = [50,100,150,300]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = MYSTERY_SHIP
        self.rect = self.image.get_rect()
        self.health = 100
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.y = 100
        self.mysteryScore = random.choice(MysteryShip.mysteryScores)
        MYSTERY_SHIP_SPRITE.add(self)
        self.speedx = 3
        # print("Added MS")

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.speedx = -self.speedx

# creates Mystery Ship
mysteryShip = MysteryShip()
