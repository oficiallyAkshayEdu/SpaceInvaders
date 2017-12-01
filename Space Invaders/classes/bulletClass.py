from classes.laserClass import *
from initializeGame import *

# inherits from Laser, which already inherits pygame sprite class
class Bullet(Laser):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__(x,y)
        self.image = BULLET
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = +20

    def update(self):
        self.rect.y += self.speedy