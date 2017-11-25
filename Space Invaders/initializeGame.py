from constants import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN)
pygame.display.set_caption("SpaceInvaders Multiplayer!")

def fontGenerator(size):
    return pygame.font.Font(SI_FONT_LOC, size)


def text_rend(string, fontDef, color):
    return fontDef.render(string, True, WHITE)

REG_FONT = pygame.font.SysFont("Arial", 20)
body_font = fontGenerator(100)
SILOGO = fontGenerator(500)
INVADERFONT = fontGenerator(36)
BULLETFONT = fontGenerator(20)

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


def draw_logo():
    LogoFont = pygame.font.Font(SI_FONT_LOC, 500)
    text_surface = LogoFont.render("A", True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT /4)
    screen.blit(text_surface,text_rect)

def draw_text( text, size, x, y):
    goFont =pygame.font.SysFont("Arial", 20)
    text_surface = goFont.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface,text_rect)


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

ALL_SPRITE_GROUPS = [CANNON_SPRITE, BULLET_SPRITE, INVADERS_ONE_SPRITE, INVADERS_TWO_SPRITE,
                     INVADERS_THREE_SPRITE, LASERS_SPRITE, SCORE_SPRITE,BLOCKER_SPRITE,
                     MYSTERY_SHIP_SPRITE, LIVES_SRPITE, LIVES_COUNTER_SPRITE]
INVADER_SPRITES = [INVADERS_ONE_SPRITE, INVADERS_TWO_SPRITE, INVADERS_THREE_SPRITE]
