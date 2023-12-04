#!/usr/bin/env python3
import pygame
from pygame.locals import *
import sys
pygame.init()

window_width = 1200
window_height = 900
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Image Cursor Copy Example")

image_path = "pokemon.png"
image = pygame.image.load(image_path)

SIZE = 64
speed = 8
# Initialize cursor position and copy surface
cursor_x, cursor_y = 0, 0
copy_surface = pygame.Surface((SIZE, SIZE))  # Adjust the size as needed
res_surf = pygame.Surface((SIZE, SIZE))
big_surf = pygame.Surface((10 * SIZE, 10 * SIZE))
big_surf.fill((255, 255, 255))
res_surf.fill((255, 255, 255))

image_y = 0
save = 0


def make_a_copy(copy_surface, res_surf):
    max_x = -1
    min_x = -1
    max_y = -1
    min_y = -1

    res_surf.fill((255, 255, 255))
    for x in range(copy_surface.get_width()):
        for y in range(copy_surface.get_height()):
            color_get = copy_surface.get_at((x, y))
            if color_get != (0, 0, 0):
                if min_x == -1 or min_x > x:
                    min_x = x
                if max_x == -1 or max_x < x:
                    max_x = x
                if min_y == -1 or min_y > y:
                    min_y = y
                if max_y == -1 or max_y < y:
                     max_y = y
                res_surf.set_at((x, y), color_get)
    print(min_x, min_y, max_x, max_y)

    return [min_x, min_y, max_x, max_y]

def make_it_big(origin, copy):
    for x in range(origin.get_width()):
        for y in range(origin.get_height()):
            current_color = origin.get_at((x, y))
            for a in range(10):
                for b in range(10):
                    big_surf.set_at((x * 10 + a, y * 10 + b), current_color)



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_LEFT:
                cursor_x -= SIZE
            elif event.key == K_RIGHT:
                cursor_x += SIZE
            elif event.key == K_UP:
                cursor_y -= SIZE
            elif event.key == K_DOWN:
                cursor_y += SIZE
            elif event.key == K_2:
                cursor_y -= 1
        if event.type == MOUSEBUTTONDOWN:
            save = 1
        
        if event.type == MOUSEMOTION:
            cursor_x, cursor_y = event.pos
            if cursor_y > 800:
                image_y -= 5
            if cursor_y < 100 and image_y < 0:
                image_y += 5


    cursor_x = max(0, min(cursor_x, window_width - 1))
    cursor_y = max(0, min(cursor_y, window_height - 1))

    screen.fill((0, 0, 0))

    screen.blit(image, (0, image_y))

    copy_rect = pygame.Rect(cursor_x, cursor_y, copy_surface.get_width(), copy_surface.get_height())
    screen.blit(big_surf, (300, 20))

    if save == 1:
        save = 0
        minmax_values = make_a_copy(copy_surface, res_surf)

        make_it_big(res_surf, big_surf)



    copy_surface.blit(screen, (0, 0), copy_rect)

    pygame.draw.rect(screen, (255, 255, 255), (cursor_x - 1, cursor_y - 1, SIZE + 2, SIZE + 2), 1)

    pygame.draw.rect(screen, (255, 255, 255), (window_width - 1 - copy_surface.get_width(), 0, SIZE + 1, SIZE + 1 ))
    screen.blit(copy_surface, (window_width - copy_surface.get_width(), 0))
    screen.blit(res_surf, (window_width - SIZE - 5, window_height - SIZE - 5))

    pygame.display.update()# Update the display


pygame.quit()
sys.exit()

