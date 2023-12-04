#!/usr/bin/env python3
import pygame
from pygame.locals import *
from collections import deque

pygame.init()

window_width = 1200
window_height = 900
screen = pygame.display.set_mode((window_width, window_height))

image_tiles = pygame.image.load("tileset.png")

SIZE = 16
x = 0
y = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_DOWN:
                y += SIZE
            elif event.key == K_UP:
                y -= SIZE
            elif event.key == K_RIGHT:
                x += SIZE
            elif event.key == K_LEFT:
                x -= SIZE


    screen.fill((0, 0, 0, 0))
    screen.blit(image_tiles, (0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (x - 1, y - 1, SIZE + 2, SIZE + 2), 1)

    pygame.display.update()# Update the display


pygame.quit()

