#!/usr/bin/env python3
import pygame
from pygame.locals import *
from collections import deque

pygame.init()


window_width = 1200
window_height = 900
screen = pygame.display.set_mode((window_width, window_height))

image_tiles = pygame.image.load("pokemon.png")

SIZE = 64
start_copy = 0

flood_surface = pygame.Surface((SIZE * 2, SIZE * 2))
flood_surface.fill((255, 255, 255, 255))
recentered_surface = pygame.Surface((SIZE, SIZE))
recentered_surface.fill((255, 255, 255, 255))
big_surface = pygame.Surface((SIZE * 8, SIZE * 8))
big_surface.fill((255, 255, 255, 255))

def copy_contiguous_pixels(x, y):
    
    start_color = screen.get_at((x, y))
    if start_color == (0, 0, 0):    # Check if the clicked pixel is not black
        return -1

    min_x = -1
    max_x = -1
    min_y = -1
    max_y = -1
    pixels_to_copy = [(x, y)]   # Create a list to store pixels to copy

    while pixels_to_copy:   #while list is not empty
        current_x, current_y = pixels_to_copy.pop()
        if (
            0 <= current_x < window_width   #be sure that pixel is on screen
            and 0 <= current_y < window_height
            and screen.get_at((current_x, current_y)) != (0, 0, 0)  #check color not black
        ):
            if min_x == -1 or current_x - x + SIZE < min_x:
                min_x = current_x - x + SIZE
            if max_x == -1 or current_x - x + SIZE > max_x:
                max_x = current_x - x + SIZE
            if min_y == -1 or current_y - y + SIZE < min_y:
                min_y = current_y - y + SIZE
            if max_y == -1 or current_y - y + SIZE > max_y:
                max_y = current_y - y + SIZE
            
            flood_surface.set_at((current_x - x + SIZE, current_y - y + SIZE), screen.get_at((current_x, current_y)))
            screen.set_at((current_x, current_y), (0, 0, 0))  # Mark the pixel as copied
            pixels_to_copy.append((current_x + 1, current_y))
            pixels_to_copy.append((current_x - 1, current_y))
            pixels_to_copy.append((current_x, current_y + 1))
            pixels_to_copy.append((current_x, current_y - 1))

    """for i in range(SIZE * 2):
        flood_surface.set_at((min_x - 1, i), (0, 255, 0))
        flood_surface.set_at((max_x + 1, i), (0, 255, 0))
        flood_surface.set_at((i, min_y - 1), (0, 255, 0))
        flood_surface.set_at((i, max_y + 1), (0, 255, 0))"""
    return (min_x, max_x, min_y, max_y)

def recenter(limits, flood_surface):
    new_surface = pygame.Surface((SIZE, SIZE))
    offset_x = int((SIZE - (limits[1] - limits[0])) / 2)
    offset_y = int((SIZE - (limits[3] - limits[2])) / 2)

    for i in range(SIZE):
        for j in range(SIZE):
            new_surface.set_at((i, j), flood_surface.get_at((limits[0] + i - offset_x, limits[2] + j - offset_y)))
    
    return new_surface

def make_it_big(origin, copy):
    for x in range(origin.get_width()):
        for y in range(origin.get_height()):
            current_color = origin.get_at((x, y))
            for a in range(4):
                for b in range(4):
                    copy.set_at((x * 4 + a, y * 4 + b), current_color)


tree_saved = 0
tree_colors = [" (Lightest)", " (light)", " (dark)", " (darkest)"]

move = 0
image_y = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                start_copy = 1

        elif event.type == MOUSEMOTION:
            cursor_x, cursor_y = event.pos
            if cursor_y > 800:
                move = 1
            elif cursor_y < 100:
                move = -1
            else:
                move = 0

    if move != 0:
        image_y -= move


    screen.fill((0, 0, 0))
    screen.blit(image_tiles, (0, image_y))

    if start_copy:
        start_copy = 0
        flood_surface.fill((0, 0, 0, 0))
        limits = copy_contiguous_pixels(mouse_pos[0], mouse_pos[1])
        if limits != -1:
            recentered_surface = recenter(limits, flood_surface)
            tree_name = "Type" + str(int(tree_saved / 4) + 1) + tree_colors[tree_saved % 4] + ".png"
            print(tree_name)
            pygame.image.save(recentered_surface, tree_name)
            tree_saved += 1
            make_it_big(flood_surface, big_surface)


    screen.blit(flood_surface, (250, 50)) 
    screen.blit(recentered_surface, (250, 200))
    screen.blit(big_surface, (400, 50)) 

    pygame.display.update()# Update the display


pygame.quit()

