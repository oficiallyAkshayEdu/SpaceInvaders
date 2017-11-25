from initializeGame import *
from classes.bulletClass import *
from classes.invaderClass import *
from classes.bulletClass import *
from classes.cannonClass import *
from classes.barricadeClass import *
from classes.mysteryShipClass import *
from classes.livesClass import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = SCORE
        self.rect = self.image.get_rect()
        self.image.fill(WHITE)
        self.rect.x = 0
        self.rect.y = 0
        self.PlayerScore = 0
        SCORE_SPRITE.add(self)

    def update(self):
        self.image = text_rend(str(self.PlayerScore), REG_FONT, WHITE)

score = Score()

class Game():

    def __init__(self):
        self.running = True
        # self.gameOver = True
        self.setup()
        # self.score = 0

    def startGame(self):
        self.main_loop()

    def setup(self):
        self.cannonSetup()
        self.invader1Setup()
        self.make_blockers()

    def invader1Setup(self):

        Invaders.initialX = 100
        InvaderArray = [rowOneInvaders, rowTwoInvaders, rowThreeInvaders]
        InvaderSpriteArray = [INVADERS_ONE_SPRITE, INVADERS_TWO_SPRITE, INVADERS_THREE_SPRITE]
        for t in range(len(InvaderArray)):
            for r in range(Invaders.rowCount):
                for i in range(Invaders.columnCount):
                    invader = InvaderArray[t]()
                    InvaderSpriteArray[t].add(invader)
            Invaders.initialX = 100

    def cannonSetup(self):
        self.cannon = Cannon()
        CANNON_SPRITE.add(self.cannon)


    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if CANNON_SPRITE:
                        self.cannon.shoot()
                    if ALL_INVADERS_SPRITE.sprites():
                        random.choice(ALL_INVADERS_SPRITE.sprites()).shoot()
            # if event.type == INVADER_DEAD:
                # print("successful event")

    def main_loop(self):
        while self.running:
            clock.tick(FPS)
            self.eventHandler()
            self.didCannonWin()
            screen.fill(BLACK)
            self.isCannonAlive()
            self.isInvaderAlive()
            self.wasBlockerHit()
            self.isLaserAlive()
            self.isMysteryShipAlive()
            self.updateSprites()
            self.drawSprites()
            pygame.display.flip()


    def updateSprites(self):
        for spriteGroup in ALL_SPRITE_GROUPS:
            spriteGroup.update()
            # print(spriteGroup.sprites())

    def drawSprites(self):
        for spriteGroup in ALL_SPRITE_GROUPS:
            spriteGroup.draw(screen)
    def didCannonWin(self):
        if not ALL_INVADERS_SPRITE:
            goScreen()
    def wasBlockerHit(self):
        blockerGotHit = pygame.sprite.groupcollide(BULLET_SPRITE, BLOCKER_SPRITE, True, True)

    def isCannonAlive(self):
        # print(LIVES_SRPITE, "OG")
        if Lives.lives == 1:
            cannonGotHit = pygame.sprite.groupcollide(BULLET_SPRITE, CANNON_SPRITE, True, True)
            if cannonGotHit:
                ALL_SPRITE_GROUPS.clear()
                goScreen()
        else:
            cannonGotHit = pygame.sprite.groupcollide(BULLET_SPRITE, CANNON_SPRITE, True, False)
        if cannonGotHit:
            for each in cannonGotHit:

                Lives.lives -=1
                updateLives()

    def isMysteryShipAlive(self):
        mysteryShipGotHit = pygame.sprite.groupcollide(LASERS_SPRITE, MYSTERY_SHIP_SPRITE, True, True)

    def isInvaderAlive(self):
        invaderGotHit = pygame.sprite.groupcollide(LASERS_SPRITE, ALL_INVADERS_SPRITE, True, True)
        if invaderGotHit:
            for each in invaderGotHit:
                for deadInvader in invaderGotHit[each]:
                    score.PlayerScore += deadInvader.scoreWorth
    def isLaserAlive(self):
        laserHitBlocker = pygame.sprite.groupcollide(LASERS_SPRITE, BLOCKER_SPRITE, True, False)
    # ablocker = Blocker(10, 4, 9)

    def make_blockers(self):
        for count in range (4):
            initialX = 50 + (count * 250)
            for row in range(5):
                for column in range(15):
                    blocker = Blocker()
                    blocker.rect.x = initialX + (column * blocker.width)
                    blocker.rect.y = 680 + (row * blocker.height)
                    BLOCKER_SPRITE.add(blocker)


def goScreen():
    ALL_SPRITE_GROUPS.clear()
    screen.fill(BLACK)
    draw_logo()
    your_score = "your Score:" + str(score.PlayerScore)
    draw_text(your_score, 60, SCREEN_WIDTH/2, SCREEN_HEIGHT * 3/4)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()