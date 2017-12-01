from initializeGame import *
from classes.gameClass import *

# defines cannon class
class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = CANNON
        self.rect = self.image.get_rect()
        self.rect.centerx = (SCREEN_WIDTH / 2)
        self.rect.bottom = (SCREEN_HEIGHT - 10)

    def update(self):
        self.speedx = 0

        # gets keystate from pygame
        keystate = pygame.key.get_pressed()

        # cannon movement code
        if keystate[pygame.K_LEFT]:
            self.speedx = -CANNON_SPEED
        elif keystate[pygame.K_RIGHT]:
            self.speedx = CANNON_SPEED
        self.rect.x += self.speedx

        # bound cannon to within screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    # on spacebar event, shoot laser
    def shoot(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        LASERS_SPRITE.add(laser)

