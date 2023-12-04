#!/usr/bin/env python3
from imports import *


def generate_old():
    background = pygame.Surface((TOTAL_TILE_SIZE, TOTAL_TILE_SIZE))
    coordinates = []
    for i in range(TILE_NUMBER):
        for j in range(TILE_NUMBER):
            coordinates.append((i, j))

    while len(coordinates) > 0:
        random_tile = possible_tiles[random.choice(list(possible_tiles.keys()))]
        index = random.randint(0, len(coordinates) - 1)
        random_place = coordinates[index]
        background.blit(get_a_tile(random_tile[0], random_tile[1]), tuple(x * TILE_SIZE for x in random_place))
        coordinates.pop(index)
    return background

def find_least_enthropy(tiles):
    current_min = -1
    mins_list = []
    for lines in range(len(tiles)):
        for col in range(len(tiles[0])):
            if tiles[lines][col] != -1:
                if current_min == -1 or current_min > len(tiles[lines][col]):
                    current_min = len(tiles[lines][col])
                    mins_list = []
                    mins_list.append((lines, col))
                elif current_min == len(tiles[lines][col]):
                    mins_list.append((lines, col))
    return mins_list

def compatibility_test(val1, val2):
    if val1 == val2:
        if val1 == border:
            return 0
        return 1
    else:
        if val1 == border and val2 == floor:
            return 1
        if val1 == floor and val2 == border:
            return 1
        return 0

def sub_function(tiles, tile_key, coo, side):
    if coo[0] < 0 or coo[1] < 0 or coo[0] > 19 or coo[1] > 19: 
        return
    if tiles[coo[0]][coo[1]] == -1:
        return
    keys_to_remove = []
    other_side = (side + 2) % 4
    for current_key, values in tiles[coo[0]][coo[1]].items():
        if not compatibility_test(tile_borders[tile_key][side], tile_borders[current_key][other_side]):
            keys_to_remove.append(current_key)
    
    while len(keys_to_remove) > 0:
        tiles[coo[0]][coo[1]].pop(keys_to_remove[0])
        keys_to_remove.pop(0)

def remove_neigbourg_possibilities(tiles, key, coo):
    sub_function(tiles, key, (coo[0], coo[1] - 1), 0)
    sub_function(tiles, key, (coo[0] - 1, coo[1]), 1)
    sub_function(tiles, key, (coo[0], coo[1] + 1), 2)
    sub_function(tiles, key, (coo[0] + 1, coo[1]), 3)

def generate():
    background = pygame.Surface((TOTAL_TILE_SIZE, TOTAL_TILE_SIZE))
    tiles = []
    for i in range(TILE_NUMBER):
        tiles.append([])
        for j in range(TILE_NUMBER):
            tiles[i].append(possible_tiles.copy())

    n = TILE_NUMBER * TILE_NUMBER
    while n > 0:
        min_enthropy_list = find_least_enthropy(tiles)
        coo = min_enthropy_list[random.randint(0, len(min_enthropy_list) - 1)]
        keys = tiles[coo[0]][coo[1]].keys()
        if len(keys) != 0:
            choosen_key = random.choice(list(keys))
            remove_neigbourg_possibilities(tiles, choosen_key, coo)
            random_tile = tiles[coo[0]][coo[1]][choosen_key]
            background.blit(get_a_tile(random_tile[0], random_tile[1]), (coo[0] * TILE_SIZE, coo[1] * TILE_SIZE))
        tiles[coo[0]][coo[1]] = -1
        
        n -= 1
        screen.blit(background, (0, 0))
        pygame.display.update()# Update the display
        pygame.time.delay(50)

    return background

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == MOUSEBUTTONUP:
            event_x, event_y = event.pos
            for button in buttons.values():
                button.is_in(event_x, event_y)
                if button.state == 1:
                    button.color = (0, 255, 0)
                if button.state == 0:
                    button.color = (0, 0, 255)


    screen.fill((0, 0, 0, 0))

    for button in buttons.values():
        pygame.draw.rect(screen, button.color, button.rectvalue)
        screen.blit(button.text, button.text_pos)

    if buttons['regenerate'].state == 1:
        all_tiles = generate()
        buttons['regenerate'].state = 0


    screen.blit(all_tiles, (0, 0))

    for i in range(window_height):
        screen.set_at((16 * 20, i), (100, 100, 100))        #draw border between grid and side
        for j in range(20):                                 #draw grid
            if buttons['show_grid'].state:
                screen.set_at((16 * j - 1, i), (100, 100, 100))
                screen.set_at((i, 16 * j - 1), (100, 100, 100))


    pygame.display.update()# Update the display


pygame.quit()
