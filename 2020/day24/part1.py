directions = open("input.txt").read().splitlines()

tiles = dict()
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
    if (x,y) in tiles:
        tiles[(x,y)] = -1 * tiles[(x,y)]
    else:
        tiles[(x,y)] = -1
    # print((x,y), "flipped:", tiles[(x,y)])

print("part1:", list(tiles.values()).count(-1))
