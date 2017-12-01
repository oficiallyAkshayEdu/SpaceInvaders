from constants import *
import functools

# initialize pygame
pygame.init()

# initialize pygame audio mixer (for future updates when audio is incorporated)
# pygame.mixer.init()

# create pygame clock
clock = pygame.time.Clock()

# create output screen
screen = pygame.display.set_mode(SCREEN)

# set windows caption
pygame.display.set_caption("Friendly SpaceInvaders!")

# Helper functions =========================================================

# creates pygame font object
def fontGenerator(size):
    return pygame.font.Font(SI_FONT_LOC, size)

# renders argument text through generated pygame font object
def text_rend(string, fontDef, color):
    return fontDef.render(string, True, WHITE)

# font for regular game text (score etc)
REG_FONT = pygame.font.SysFont("Arial", 20)

# Helper functions =========================================================

# font for the Space Invaders Logo
SILOGO = fontGenerator(500)

# font for the invaders
INVADERFONT = fontGenerator(36)

# font for invaders bullets
BULLETFONT = fontGenerator(20)

# Text renderers =========================================================
'''
each line represents a text renderer for a specific game object.
I used a font file instead of images.
each string letter represents the letter from the font file which corresponds to the 
required image.
example: the cannon image is mapped to the letter w in the font
'''
CANNON = text_rend("w", INVADERFONT, WHITE)
BULLET = text_rend("y", BULLETFONT, WHITE)
INVADER1 = text_rend("b", INVADERFONT, WHITE)
INVADER1_ALT = text_rend("c", INVADERFONT, WHITE)
INVADER2 = text_rend("d", INVADERFONT, WHITE)
INVADER2_ALT = text_rend("e", INVADERFONT, WHITE)
INVADER3 = text_rend("f", INVADERFONT, WHITE)
INVADER3_ALT = text_rend("g", INVADERFONT, WHITE)
logo_ren = text_rend("A", SILOGO, BLACK)
SCORE = text_rend("0", REG_FONT, WHITE)
MYSTERY_SHIP = text_rend("v", INVADERFONT, WHITE)


# really wanted to learn and understand decorators, make one of my own and then use it.
def debugPrinter(func):
    @functools.wraps(func)
    def function_runner(*args):
        if VERBOSE == True:
            func(*args)
    return function_runner

@debugPrinter
def debugPrint(string):
    print(string)

# draws logo on the game over screen
def draw_logo():
    LogoFont = pygame.font.Font(SI_FONT_LOC, 500)
    text_surface = LogoFont.render("A", True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT /4)
    screen.blit(text_surface,text_rect)

# draws supplied text on the game over screen
def draw_text( text, size, x, y):
    goFont =pygame.font.SysFont("Arial", 20)
    text_surface = goFont.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface,text_rect)

# helper function to enable left right oscialltion of invders and muysteryship
def ObjOsc(object):
    object.rect.x += object.__class__. SPEED
    debugPrint(object.rect.x)
    if object.rect.right >= SCREEN_WIDTH or object.rect.left <= 0:
        object.__class__.SPEED = -object.__class__.SPEED

# initializes the sprite groups
CANNON_SPRITE = pygame.sprite.Group()
BULLET_SPRITE = pygame.sprite.Group()
ALL_INVADERS_SPRITE = pygame.sprite.Group()
INVADERS_ONE_SPRITE = pygame.sprite.Group()
INVADERS_TWO_SPRITE = pygame.sprite.Group()
INVADERS_THREE_SPRITE = pygame.sprite.Group()
LASERS_SPRITE = pygame.sprite.Group()
SCORE_SPRITE = pygame.sprite.Group()
BLOCKER_SPRITE = pygame.sprite.Group()
MYSTERY_SHIP_SPRITE = pygame.sprite.Group()
LIVES_SRPITE = pygame.sprite.Group()
LIVES_COUNTER_SPRITE = pygame.sprite.Group()
GAMEOVER_SPRITE = pygame.sprite.Group()

# manually constructed list of all sprite groups
# used to iterate over and update and draw each sprite group
ALL_SPRITE_GROUPS = [CANNON_SPRITE, BULLET_SPRITE, INVADERS_ONE_SPRITE, INVADERS_TWO_SPRITE,
                     INVADERS_THREE_SPRITE, LASERS_SPRITE, SCORE_SPRITE,BLOCKER_SPRITE,
                     MYSTERY_SHIP_SPRITE, LIVES_SRPITE, LIVES_COUNTER_SPRITE]

# subset of above list
INVADER_SPRITES = [INVADERS_ONE_SPRITE, INVADERS_TWO_SPRITE, INVADERS_THREE_SPRITE]
