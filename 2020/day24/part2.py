from collections import defaultdict
directions = open("input.txt").read().splitlines()

BLACK = True
WHITE = False

tiles = defaultdict(lambda: False)
while directions:
    x, y = 0, 0
    dirs = list(directions.pop())
    # print(dirs)
    while dirs:
        d = dirs.pop(0)
        if d == 'e':
            x += 2
        elif d == 'w':
            x -= 2
        elif d == 's':
            y -= 2
            d = dirs.pop(0)
            if d == 'e':
                x += 1
            elif d == 'w':
                x -= 1
        elif d == 'n':
            y += 2
            d = dirs.pop(0)
            if d == 'e':
                x += 1
            elif d == 'w':
                x -= 1
    tiles[(x,y)] = not tiles[(x,y)]
    # print((x,y), "flipped:", tiles[(x,y)])

print("part1:", list(tiles.values()).count(BLACK), '\n')

for day in range(1, 101):
    tmp = tiles.copy()
    for tile, value in tmp.items():
        # necessary to preinitialize tiles that may flip
        if value == BLACK:
            for x,y in ((sum(x) for x in zip(tile, d))
                    for d in ((2,0),(-2,0),(1,2),(1,-2),(-1,2),(-1,-2))):
                _ = tiles[(x,y)]
    state = tiles.copy()
    for tile, value in tiles.items():
        if value == BLACK:
            dirs = ((sum(x) for x in zip(tile, d))
                for d in ((2,0),(-2,0),(1,2),(1,-2),(-1,2),(-1,-2)))
            adjacent = len([BLACK for x,y in dirs if tmp[(x,y)] == BLACK])
            if adjacent == 0:
                del state[tile] # can't flip if adjacent tiles are white
            elif adjacent > 2:
                state[tile] = WHITE
        elif value == WHITE:
            dirs = ((sum(x) for x in zip(tile, d))
                for d in ((2,0),(-2,0),(1,2),(1,-2),(-1,2),(-1,-2)))
            adjacent = len([BLACK for x,y in dirs if tmp[(x,y)] == BLACK])
            if adjacent == 0:
                del state[tile] # can't flip if adjacent tiles are white
            elif adjacent == 2:
                state[tile] = BLACK
    tiles = state.copy()
    if day in range(10) or day%10 == 0:
        print("day", day, "-", list(tiles.values()).count(BLACK))

print('\n' + "part2:", list(tiles.values()).count(BLACK))
