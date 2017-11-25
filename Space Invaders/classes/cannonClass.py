from initializeGame import *
from classes.gameClass import *




class Cannon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = CANNON
        self.rect = self.image.get_rect()
        self.rect.centerx = (SCREEN_WIDTH / 2)
        self.rect.bottom = (SCREEN_HEIGHT - 10)
        self.score = 0
        self.lives = 5
        self.alive = True
        self.name = ""



    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -PLAYER_SPEED
        elif keystate[pygame.K_RIGHT]:
            self.speedx = PLAYER_SPEED
        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH


    def shoot(self):
        laser = Laser(self.rect.centerx, self.rect.top)
        LASERS_SPRITE.add(laser)

