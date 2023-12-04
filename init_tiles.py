import random
from tile_dictionaries import *
from models import *


def init_tiles():

    original_dict_of_tiles = {}
    for i in range(20):
        for j in range(20):
            original_dict_of_tiles[str(i) + "." + str(j)] = tile_generation(possible_tiles, i, j, possibility_number)
    return original_dict_of_tiles


possibility_number = len(possible_tiles)
lowest_possibility = possibility_number
original_dict_of_tiles = init_tiles()
Dict_of_tiles = original_dict_of_tiles.copy()

def pick_tile():
    lowest_possibilities_tiles = []
    for key, tile in Dict_of_tiles.items():
        if tile.possibilities == lowest_possibility:
            lowest_possibilities_tiles.append(tile)
    pick = random.randint(0, len(lowest_possibilities_tiles) - 1)
    
    return lowest_possibilities_tiles[pick]

def change_neigbour_possibilities(key, x, y):
    if y != 19:
        for tiles in incompatibilities[key][2]:
            if tiles in original_dict_of_tiles[str(x) + "." + str(y + 1)].possible_tiles.keys():
                original_dict_of_tiles[str(x) + "." + str(y + 1)].possible_tiles.pop(tiles)
    if x != 19:
        for tiles in incompatibilities[key][3]:
            if tiles in original_dict_of_tiles[str(x + 1) + "." + str(y)].possible_tiles.keys():
                original_dict_of_tiles[str(x + 1) + "." + str(y)].possible_tiles.pop(tiles)


def regenerate():
    all_tiles = pygame.Surface((16 * 20, 16 * 20))
    original_dict_of_tiles = init_tiles()


    possibility_number = len(possible_tiles)
    lowest_possibility = possibility_number
    original_dict_of_tiles = init_tiles()
    Dict_of_tiles = original_dict_of_tiles.copy()
    
    while len(Dict_of_tiles) != 0:
        tile = pick_tile()
        random_key = random.choice(list(tile.possible_tiles.keys()))
        first_tile = get_a_tile(possible_tiles[random_key][0], possible_tiles[random_key][1])
        all_tiles.blit(first_tile, (tile.x * 16, tile.y * 16))

        change_neigbour_possibilities(random_key, tile.x, tile.y)
        Dict_of_tiles.pop(str(tile.x) + "." + str(tile.y))

        screen.blit(all_tiles, (0, 0))
        pygame.display.update()# Update the display
        pygame.time.delay(10)
    return all_tiles


"""for i in range(20):
    for j in range(20):
        random_key = random.choice(list(possible_tiles.keys()))
        first_tile = get_a_tile(possible_tiles[random_key][0], possible_tiles[random_key][1])
        #first_tile = get_a_tile(random.randint(0, 56), random.randint(0, 51))
        all_tiles.blit(first_tile, (i * 16, j * 16))"""