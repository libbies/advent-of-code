from collections import defaultdict
from copy import deepcopy
directions = open("input.txt").read().splitlines()

BLACK = -1
WHITE = 1

tiles = defaultdict(lambda: 1)
while directions:
    x, y = 0, 0
    dirs = list(directions.pop())
    # print(dirs)
    while dirs:
        d = dirs.pop(0)
        if d == 'e':
            x += 1
        elif d == 'w':
            x -= 1
        elif d == 's':
            y -= 1
            d = dirs.pop(0)
            if d == 'e':
                x += 0.5
            elif d == 'w':
                x -= 0.5
        elif d == 'n':
            y += 1
            d = dirs.pop(0)
            if d == 'e':
                x += 0.5
            elif d == 'w':
                x -= 0.5
    tiles[(x,y)] = -1 * tiles[(x,y)]
    # print((x,y), "flipped:", tiles[(x,y)])

print("part1:", list(tiles.values()).count(BLACK), '\n')

for day in range(1, 101):
    tmp = deepcopy(tiles)
    for tile, value in tmp.items():
        # necessary to preinitialize tiles that may flip
        if value == BLACK:
            for x,y in ((sum(x) for x in zip(tile, d))
                    for d in ((1,0),(-1,0),(0.5,1),(0.5,-1),(-0.5,1),(-0.5,-1))):
                _ = tiles[(x,y)]
    state = deepcopy(tiles)
    for tile, value in tiles.items():
        if value == BLACK:
            dirs = ((sum(x) for x in zip(tile, d))
                for d in ((1,0),(-1,0),(0.5,1),(0.5,-1),(-0.5,1),(-0.5,-1)))
            adjacent = len([BLACK for x,y in dirs if tmp[(x,y)] == BLACK])
            if 0 == adjacent:
                del state[tile] # can't flip if adjacent tiles are white
            elif adjacent > 2:
                state[tile] = WHITE
        elif value == WHITE:
            dirs = ((sum(x) for x in zip(tile, d))
                for d in ((1,0),(-1,0),(0.5,1),(0.5,-1),(-0.5,1),(-0.5,-1)))
            adjacent = len([BLACK for x,y in dirs if tmp[(x,y)] == BLACK])
            if adjacent == 0:
                del state[tile] # can't flip if adjacent tiles are white
            elif adjacent == 2:
                state[tile] = BLACK
    tiles = deepcopy(state)
    if day in range(10) or day%10 == 0:
        print(f"day {day}:", list(tiles.values()).count(-1))

print('\n' + "part2:", list(tiles.values()).count(-1))
