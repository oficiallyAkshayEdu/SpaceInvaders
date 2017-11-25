from initializeGame import *


def updateLives():
    LIVES_SRPITE.empty()
    Lives.initialX = 50
    for i in range(Lives.lives):
        lives = Lives()
        LIVES_SRPITE.add(lives)

class Lives(pygame.sprite.Sprite):

    initialX = 50
    lives = 10

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = CANNON
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - 120
        self.rect.x = Lives.initialX
        self.width = 40
        self.createRow()
        LIVES_SRPITE.add(self)

    def createRow(self):
        Lives.initialX += self.width
        print("created)")


for i in range(Lives.lives):
    lives = Lives()
    LIVES_SRPITE.add(lives)

class LivesCounter(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = SCORE
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = SCREEN_HEIGHT -20
        LIVES_COUNTER_SPRITE.add(self)

    def update(self):
        self.image = text_rend(str(Lives.lives), REG_FONT, WHITE)

livesCounter = LivesCounter()


class GameOver(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = logo_ren
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH /2
        self.rect.centery = SCREEN_HEIGHT /2
        GAMEOVER_SPRITE.add(self)

    def update(self):
        screen.fill(BLACK)
        self.image = text_rend("A", SILOGO, WHITE)

gameOver = GameOver()

