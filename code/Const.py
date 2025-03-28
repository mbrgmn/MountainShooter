# C
import pygame

COLOR_YELLOW = (250, 255, 107)
COLOR_WHITE = (255, 255, 255)
COLOR_BROWN = (69, 39, 25)
COLOR_BLUE = (69, 10, 212)
COLOR_RED = (237, 9, 45)
COLOR_PURPLE = (122, 0, 222)

# E
ENEMY_EVENT = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

# L
ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
#    'level2bg0': 999,
#    'level2bg1': 999,
#    'level2bg2': 999,
#    'level2bg3': 999,
#    'level2bg4': 999,
    'Player1': 300,
#    'Player1shot': 1,
    'Player2': 300,
#    'Player2shot': 1,
    'Enemy1': 50,
#    'Enemy1shot': 1,
    'Enemy2': 50,
#    'Enemy2shot': 1,
}


# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}
# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
