import pygame as pg

# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = r'PNG\Tiles\tile_196.png'

# player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 2.5
PLAYER_IMG = 'PNG\Hitman 1\hitman1_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)

# mob settings
MOB_IMG = 'PNG\Zombie 1\zoimbie1_hold.png'