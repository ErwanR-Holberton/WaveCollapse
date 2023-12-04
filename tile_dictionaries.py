
all_waters = {
'Water top left': (0, 42),
'Water midle left': (0, 43),
'Water bottom left': (0, 44),
'Water top midle': (1, 42),
'Water midle midle': (1, 43),
'Water bottom midle': (1, 44),
'Water top right': (2, 42),
'Water midle right': (2, 43),
'Water bottom right': (2, 44),
}
floor = 1
any = 0
water = 2
corner_up = 3
corner_down = 4
corner_left = 5
corner_right = 6
border = 7
road = 8
tile_borders = {}
tile_borders['Grass'] = [floor, floor, floor, floor]
tile_borders['Water top left'] = [border, border, corner_left, corner_up]
tile_borders['Water midle left'] = [corner_left, border, corner_left, water]
tile_borders['Water bottom left'] = [corner_left, border, border, corner_down]
tile_borders['Water top midle'] = [border, corner_up, water, corner_up]
tile_borders['Water midle midle'] = [water, water, water, water]
tile_borders['Water bottom midle'] = [water, corner_down, border, corner_down]
tile_borders['Water top right'] = [border, corner_up, corner_right, border]
tile_borders['Water midle right'] = [corner_right, water, corner_right, border]
tile_borders['Water bottom right'] = [corner_right, corner_down, border, border]

"""tile_borders['Road top left']     = [floor, floor, road, road]
tile_borders['Road midle left']   = [road, floor, road, road]
tile_borders['Road bottom left']  = [road, floor, floor, road]
tile_borders['Road top midle']    = [floor, road, road, road]
tile_borders['Road center']       = [road, road, road, road]
tile_borders['Road bottom midle'] = [road, road, floor, road]
tile_borders['Road top right']    = [floor, road, road, floor]
tile_borders['Road midle right']  = [road, road, road, floor]
tile_borders['Road bottom right'] = [road, road, floor, floor]"""

possible_tiles = {}
possible_tiles['Grass'] = (51, 36)
possible_tiles['Water top left'] = (0, 42)
possible_tiles['Water midle left'] = (0, 43)
possible_tiles['Water bottom left'] = (0, 44)
possible_tiles['Water top midle'] = (1, 42)
possible_tiles['Water midle midle'] = (1, 43)
possible_tiles['Water bottom midle'] = (1, 44)
possible_tiles['Water top right'] = (2, 42)
possible_tiles['Water midle right'] = (2, 43)
possible_tiles['Water bottom right'] = (2, 44)

"""possible_tiles['Road top left']     = (0, 45)
possible_tiles['Road midle left']   = (0, 46)
possible_tiles['Road bottom left']  = (0, 47)
possible_tiles['Road top midle']    = (1, 45)
possible_tiles['Road center']       = (1, 46)
possible_tiles['Road bottom midle'] = (1, 47)
possible_tiles['Road top right']    = (2, 45)
possible_tiles['Road midle right']  = (2, 46)
possible_tiles['Road bottom right'] = (2, 47)"""

white_list = {}
for keys in possible_tiles.keys():
    white_list[keys] = {'above': {}, 'to_left': {}, 'under': {}, 'to_right': {}}


rules = {'above': {}, 'to_left': {}, 'under': {}, 'to_right': {}}
for key in all_waters.keys():
    if key != 'Water top midle':
        rules['above'][key] = 'Grass'
#print(rules)

incompatibilities = {}
incompatibilities['Road'] = [[], [], [], []]
incompatibilities['Water top left'] = [['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], ['Grass'], ['Grass']]
incompatibilities['Grass'] = [[], [], [], []]
incompatibilities['Water midle left'] = [[], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], [], []]
incompatibilities['Water bottom left'] = [[], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], []]
incompatibilities['Water top midle'] = [['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], [], [], []]
incompatibilities['Water midle midle'] = [[], [], [], []]
incompatibilities['Water bottom midle'] = [[], [], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], []]
incompatibilities['Water top right'] = [['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], [], [], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right']]
incompatibilities['Water midle right'] = [[], [], [], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right']]
incompatibilities['Water bottom right'] = [[], [], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right'], ['Water top left', 'Water midle left', 'Water bottom left', 'Water top midle', 'Water midle midle', 'Water bottom midle', 'Water top right', 'Water midle right', 'Water bottom right']]


