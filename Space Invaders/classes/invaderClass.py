from initializeGame import *
from classes.bulletClass import *

# defining the Invader parent class
class Invaders(pygame.sprite.Sprite):

    columnCount = 11  # number of invaders we want in each row
    initialX = 100  # starting x value of the first invader
    initialY = 150  # initial Y of the first row of invaders

    # computation to always center the invader sin the screen
    total_width = SCREEN_WIDTH - (initialX*2)
    width = total_width/(columnCount)
    SPEED = INVADER_SPEED

    # housekeeping counters for various functions
    i = 0
    count =0
    rowCount= 1


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.speedy = 0  # Todo add code for vertical movement of invaders as well
        self.createRow()  # fx to create correct number of rows of Invaders
        self.rowCount = 2  # sets initial number of rows for each invader type to 2 (overriden later

        # adds self to ALL Invader sprites. Needed to determine rnadom shooter and if game over
        ALL_INVADERS_SPRITE.add(self)

    def createRow(self):
        invaderCount = str(Invaders.count) + "the Count of Invaders"
        debugPrint(invaderCount)

        # for every 11 invaders, reset to new row
        if Invaders.count % Invaders.columnCount == 0:
            Invaders.initialX = 100
            Invaders.initialY += 50
            debugPrint(Invaders.initialY)
        else:
            Invaders.initialX += self.width
        Invaders.count +=1

    # instantiates new bullet on spacebar event
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        BULLET_SPRITE.add(bullet)

    # update loop
    def update(self):
        # oscillate self
        ObjOsc(self)
        # animate self
        self.animate()

    # housekeeping function to enable animation at interval
    def advanceI(self):
        if self.i >= FPS*2:
            self.i = 0
        else:
            self.i +=1

    # switches sprites every specific interval
    def animate(self):
        if self.i in (0,FPS):
            self.image = self.altimage
        elif self.i in (FPS+1, FPS*2):
            self.image = self.ogimage
        self.advanceI()

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
        self.altimage = INVADER1_ALT
        self.ogimage = INVADER1
        Invaders.rowCount =2

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
        self.altimage = INVADER2_ALT
        self.ogimage = INVADER2

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
        self.altimage = INVADER3_ALT
        self.ogimage = INVADER3