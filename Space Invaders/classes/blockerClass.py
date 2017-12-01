from initializeGame import *

# define the blocker class
class Blocker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.height = self.width = 10  # set smallest unit size to a square
        self.image = pygame.Surface((self.width, self.height))  # creates surface of self size
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        screen.blit(self.image, self.rect) # blits blocker to screen each frame



