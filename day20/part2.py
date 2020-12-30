# import code
import numpy as np
from math import sqrt
from pprint import pprint

def rotate(t, rotations=0):
    if rotations >= 4:
        t = np.fliplr(t)
    for r in range(rotations%4):
        t = np.rot90(t)
    return t

def get_edges(t, rotations=0):
    """binary -> decimal, so i can actually read the numbers ;_;"""
    t = rotate(t, rotations)
    return (
        int(''.join(t[0]), 2), # top
        int(''.join(r[-1] for r in t), 2), # right
        int(''.join(t[-1]), 2), # bottom
        int(''.join(r[0] for r in t), 2), # left
    )

filename = "input.txt"
tiles = dict()
for lines in map(str.split, open(filename).read().split('\n\n')):
    # print(tile)
    tiles[int(lines[1][:-1])] = [
        lines[2],
        ''.join(r[-1] for r in lines[2:]),
        lines[-1],
        ''.join(r[0] for r in lines[2:]),
    ]

part1 = 1
corners = dict()
edges = dict()
inner = dict()
for id, tile in tiles.items():
    matches = list()
    for edge in tile:
        matches += [k for k, v in tiles.items() if k!=id and edge in v or edge[::-1] in v]
        # print(id, edge, len(match), match)
    if len(matches) == 2:
        corners[id] = matches
        part1 *= id
    elif len(matches) == 3:
        edges[id] = matches
    else:
        inner[id] = matches

print("part1:", part1)

# pprint(("corners:", len(corners), corners))
# pprint(("edges:", len(edges), edges))

l = int(sqrt(len(tiles)))
grid = [[None for i in range(l)] for i in range(l)]

### upper left corner
grid[0][0] = [*corners][0]

### top edge of image
for n in range(1, l-1):
    grid[0][n] = next(
        k for k, v in edges.items()
        if grid[0][n-1] in v
        if k not in grid[0]
    )

### upper right corner
grid[0][-1] = next(
    k for k,v in corners.items()
    if grid[0][-2] in v
)

### left edge of image
for n in range(1, l-1):
    grid[n][0] = next(
        k for k,v in edges.items()
        if grid[n-1][0] in v
        if k not in (c for row in grid for c in row)
    )

### lower left corner
grid[-1][0] = next(
    k for k,v in corners.items()
    if grid[-2][0] in v
)

### right edge of image
for n in range(1, l-1):
    grid[n][-1] = next(
        k for k,v in edges.items()
        if grid[n-1][-1] in v
        if k not in (c for row in grid for c in row)
    )

### top edge of image
for n in range(1, l-1):
    grid[-1][n] = next(
        k for k, v in edges.items()
        if grid[-1][n-1] in v
        if k not in (c for row in grid for c in row)
    )

### lower right corner
grid[-1][-1] = next(
    k for k,v in corners.items()
    if grid[-2][-1] in v
    and grid[-1][-2] in v
)

### interior of image
for x in range(1, l-1):
    for y in range(1, l-1):
        grid[x][y] = next(
            k for k,v in inner.items()
            if grid[x-1][y] in v
            and grid[x][y-1] in v
            if k not in (c for row in grid for c in row)
        )

pprint(grid)

tiles = dict()
for lines in map(str.split, open(filename).read().replace('.', '0').replace('#', '1').split('\n\n')):
    # print(tile)
    tiles[int(lines[1][:-1])] = np.array([list(row) for row in lines[2:]])

image = [[None for i in range(l)] for i in range(l)]
for x in range(l):
    for y in range(l):
        image[x][y] = tiles[grid[x][y]]

image = np.array(image)


# now that we have the grid ids,
# we have to rotate/mirror tiles to get the correct alignment
# each tile needs two adjacent matches to orient the tile
# so we can put the top 2x2 in place first
# and then figure out the rest using the 2x2 as guides
TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3
for c00 in range(8):
    for c01 in range(8):
        for c10 in range(8):
            for c11 in range(8):
                if (get_edges(image[0,0], c00)[RIGHT] == get_edges(image[0,1], c01)[LEFT]
                        and get_edges(image[0,0], c00)[BOTTOM] == get_edges(image[1,0], c10)[TOP]
                        and get_edges(image[0,1], c01)[BOTTOM] == get_edges(image[1,1], c11)[TOP]
                        and get_edges(image[1,0], c10)[RIGHT] == get_edges(image[1,1], c11)[LEFT]):
                    # print(c00, c01, c10, c11)
                    image[0,0] = rotate(image[0,0], c00)
                    image[0,1] = rotate(image[0,1], c01)
                    image[1,0] = rotate(image[1,0], c10)
                    image[1,1] = rotate(image[1,1], c11)
                    break

# finish the top two rows of the image
for y in range(2, l):
    for r0 in range(8):
        for r1 in range(8):
            if (get_edges(image[0,y-1])[RIGHT] == get_edges(image[0,y], r0)[LEFT]
                    and get_edges(image[1,y-1])[RIGHT] == get_edges(image[1,y], r1)[LEFT]
                    and get_edges(image[0,y], r0)[BOTTOM] == get_edges(image[1,y], r1)[TOP]):
                # print(y, r0, r1)
                image[0,y] = rotate(image[0,y], r0)
                image[1,y] = rotate(image[1,y], r1)
                break

# and all of the remaining rows
for x in range(2, l):
    for y in range(0, l, 2):
        for c0 in range(8):
            for c1 in range(8):
                if (get_edges(image[x-1,y])[BOTTOM] == get_edges(image[x,y], c0)[TOP]
                        and get_edges(image[x-1,y+1])[BOTTOM] == get_edges(image[x,y+1], c1)[TOP]
                        and get_edges(image[x,y], c0)[RIGHT] == get_edges(image[x,y+1], c1)[LEFT]):
                    # print(x, y, c0, c1)
                    image[x,y] = rotate(image[x,y], c0)
                    image[x,y+1] = rotate(image[x,y+1], c1)
                    break

# ok, now that we have the grid, we strip the borders
lines = list()
for x in range(l):
    for r in range(1, len(image[x,0])-1):
        lines.append(np.concatenate([image[x,y][r][1:-1] for y in range(l)]))

lines = np.array(lines)

# beyond here be dragons
# '01234567890123456789'
#0'                  # '
#1'#    ##    ##    ###'
#2' #  #  #  #  #  #   '

dragons = 0
l = len(lines)
for r in range(8):
    image = rotate(lines, r)
    for x in range(l-2):
        for y in range(l-19):
            if ('1' == image[x,y+18]
                    == image[x+1,y]
                    == image[x+1,y+5]
                    == image[x+1,y+6]
                    == image[x+1,y+11]
                    == image[x+1,y+12]
                    == image[x+1,y+17]
                    == image[x+1,y+18]
                    == image[x+1,y+19]
                    == image[x+2,y+1]
                    == image[x+2,y+4]
                    == image[x+2,y+7]
                    == image[x+2,y+10]
                    == image[x+2,y+13]
                    == image[x+2,y+16]):
                # print("whee, a dragon")
                dragons += 1

print(f"{dragons} dragons found, covering {15*dragons} #s")

print(f"{np.unique(lines, return_counts=True)[-1][-1]} - {15*dragons}"
      f" = part2: {np.unique(lines, return_counts=True)[-1][-1]-15*dragons}")

# code.interact(local=dict(globals(), **locals()))
