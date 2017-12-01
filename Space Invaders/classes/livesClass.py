from initializeGame import *

# defines livesUpdater
def updateLives():
    LIVES_SRPITE.empty()
    Lives.initialX = 50
    for i in range(Lives.lives):
        lives = Lives()
        LIVES_SRPITE.add(lives)

# creates Lives sprite area
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
        debugPrint("created)")

# creates n number o flives
for i in range(Lives.lives):
    lives = Lives()
    LIVES_SRPITE.add(lives)

# creates lives counter (number only sprite region
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


# creates livesCounter object
livesCounter = LivesCounter()

