from initializeGame import *
from classes.bulletClass import *


class Invaders(pygame.sprite.Sprite):
    columnCount = 11
    initialX = 100
    total_width = SCREEN_WIDTH - (initialX*2)
    width = total_width/(columnCount)
    i = 0
    initialY = 150
    count =0
    rowCount= 1

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speedx = 5
        self.speedy = 0
        self.createRow()
        self.rowCount = 2
        # self.count = 0
        ALL_INVADERS_SPRITE.add(self)


    def createRow(self):
        print(Invaders.count, "thecount")
        if Invaders.count % 11 == 0:
            Invaders.initialX = 100
            Invaders.initialY += 50
            print(Invaders.initialY)
        else:
            Invaders.initialX += self.width

        Invaders.count +=1
        # Invaders.initialX = 100
            # self.Sprite.add(self)

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        BULLET_SPRITE.add(bullet)

    def updater(self):
        self.rect.x += self.speedx
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            for each in self.Sprite:
                each.speedx = -each.speedx

    def advanceI(self):
        if self.i >= FPS*2:
            self.i = 0
        else:
            self.i +=1

class rowOneInvaders(Invaders):

    def __init__(self):
        super().__init__()
        self.Sprite = INVADERS_ONE_SPRITE
        self.scoreWorth = 10
        self.image = INVADER1
        self.rect = self.image.get_rect()
        self.rect.centerx = Invaders.initialX
        self.rect.y = 170
        self.Sprite.add(self)
        self.rowCount = 1
        self.count = 0
        Invaders.rowCount =2

    def update(self):
        self.updater()
        if self.i in (0,FPS):
            self.image = INVADER1_ALT
        elif self.i in (FPS+1, FPS*2):
            self.image = INVADER1
        self.advanceI()


class rowTwoInvaders(Invaders):
    def __init__(self):
        super().__init__()
        Invaders.rowCount = 2
        self.image = INVADER2
        self.Sprite = INVADERS_TWO_SPRITE
        self.rect = self.image.get_rect()
        self.scoreWorth = 20
        self.rect.centerx = Invaders.initialX
        self.rect.y = Invaders.initialY
        self.Sprite.add(self)
        self.rowCount = 2
        self.count = 0


    def update(self):
        self.updater()
        if self.i in (0,FPS/2) or self.i in (FPS*(3/4), FPS):
            self.image = INVADER2
        elif self.i in ((FPS/2)+1, FPS*(3/4)):
            self.image = INVADER2_ALT
        self.advanceI()

class rowThreeInvaders(Invaders):
    def __init__(self):
        super().__init__()
        Invaders.rowCount = 2
        self.Sprite = INVADERS_THREE_SPRITE
        self.scoreWorth = 30
        self.image = INVADER3
        self.rect = self.image.get_rect()
        self.rect.centerx = Invaders.initialX
        self.rect.y = Invaders.initialY
        self.Sprite.add(self)
        self.rowCount = 2
        self.count = 0

    def update(self):
        self.updater()
        if self.i in (0, FPS):
            self.image = INVADER3_ALT
        elif self.i in (FPS+1, FPS*2):
            self.image = INVADER3
        self.advanceI()
