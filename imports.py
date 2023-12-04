import pygame
pygame.init()

from pygame.locals import *
import random

from models import *
from tile_dictionaries import *
from modules import *

TILE_SIZE = 16
TILE_NUMBER = 20
TOTAL_TILE_SIZE = TILE_SIZE * TILE_NUMBER
window_width = 16 * 20 + 300
window_height = 16 * 20
screen = pygame.display.set_mode((window_width, window_height))

image_tiles = pygame.image.load("tileset.png")

def get_a_tile(x, y):
    if x < 0 or y < 0 or x > 56 or y > 51:
        return None
    tile = pygame.Surface((16, 16))
    for i in range(16):
        for j in range(16):
            tile.set_at((i, j), image_tiles.get_at((x * 16 + i, y * 16 + j)))
    return tile

buttons = {}
buttons['show_grid']  = Button("show grid")
buttons['regenerate'] = Button("regenerate")
buttons['regenerate'].state = 0

all_tiles = pygame.Surface((16 * 20, 16 * 20))

clear_terminal()