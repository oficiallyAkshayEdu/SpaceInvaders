from initializeGame import *

class Blocker(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.height = self.width = 10
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()

    def update(self):
        screen.blit(self.image, self.rect)



