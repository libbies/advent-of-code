#!/usr/bin/env python3
import sys
import numpy
from pprint import pprint

# https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
def gcd(a,b):
    """Compute the greatest common divisor of and b"""
    while b > 0:
        a, b = b, a % b
    return a

def intpoints(pointa, pointb):
    ax, ay = pointa
    bx, by = pointb
    div = gcd(abs(bx - ax), abs(by - ay))
    dx = (bx - ax) // div
    dy = (by - ay) // div
    # print(f"a:{ax},{ay} b:{bx},{by} div:{div}, dx:{dx}, dy:{dy}")
    # print(f"%{(bx - ax) % div} %{(by - ay) % div}")
    if (bx - ax) % div != 0 or (by - ay) % div != 0:
        return [pointa, pointb]
    # print(f"a:{ax},{ay} b:{bx},{by} div:{div}, dx:{dx}, dy:{dy}")
    # if dx == 0 or dy == 0:
    #     return [pointa, pointb]
    points = list()
    if div >= 1 and dx != 0 and dy != 0:
        for n in range(0, div+1):
            points += [(ax+(dx*n), ay+(dy*n))]
    elif div <= 1 and dx != 0 and dy != 0:
        for n in range(0, div-1, -1):
            points += [(ax+(dx*n), ay+(dy*n))]
            points += [(ax+(dx*n), ay+(dy*n))]
    else:
        print(f"a:{ax},{ay} b:{bx},{by} div:{div}, dx:{dx}, dy:{dy}")
        raise(StopIteration)
    return sorted(set(points))

def count(placemap, x, y):
    h, w = placemap.shape
    count = 0
    # up
    if 1 in placemap[0:x, y]:
        count += 1
    # down
    if 1 in placemap[x+1:h, y]:
        count += 1
    # left
    if 1 in placemap[x, 0:y]:
        count += 1
    # right
    if 1 in placemap[x, y+1:h]:
        count += 1
    candidates = numpy.copy(placemap)
    candidates[x, 0:w] = -1
    candidates[0:h, y] = -2
    candidates[x, y] = -99
    # x:0->x, y:0->y
    for _x in range(x):
        for _y in range(y):
            if candidates[_x,_y] != 1:
                continue
            # print(f"_x/_y:{_x},{_y} x/y:{x},{y} points:{intpoints((_x,_y), (x,y))}")
            if 1 in candidates[tuple(zip(*intpoints((_x,_y), (x,y))))]:
                count += 1
                candidates[tuple(zip(*intpoints((_x,_y), (x,y))))] = -3 # * _x * _y
    # x:x->h, y:0->y
    for _x in range(h-1, x, -1):
        for _y in range(y):
            if candidates[_x,_y] != 1:
                continue
            # print(f"_x/_y:{_x},{_y} x/y:{x},{y} points:{intpoints((_x,_y), (x,y))}")
            if 1 in candidates[tuple(zip(*intpoints((_x,_y), (x,y))))]:
                count += 1
                candidates[tuple(zip(*intpoints((_x,_y), (x,y))))] = -4 # * _x * _y
    for _x in range(x):
        for _y in range(w-1, y, -1):
            if candidates[_x,_y] != 1:
                continue
            # print(f"_x/_y:{_x},{_y} x/y:{x},{y} points:{intpoints((_x,_y), (x,y))}")
            if 1 in candidates[tuple(zip(*intpoints((_x,_y), (x,y))))]:
                count += 1
                candidates[tuple(zip(*intpoints((_x,_y), (x,y))))] = -5 # * _x * _y
    # x:x->h, y:y->h
    for _x in range(h-1, x, -1):
        for _y in range(w-1, y, -1):
            if candidates[_x,_y] != 1:
                continue
            # print(f"! _x/_y:{_x},{_y} x/y:{x},{y} points:{intpoints((_x,_y), (x,y))} cs:{-6 * _x * -y}")
            if 1 in candidates[tuple(zip(*intpoints((_x,_y), (x,y))))]:
                count += 1
                candidates[tuple(zip(*intpoints((_x,_y), (x,y))))] = -6 * (_x+1) * (_y+1)
    candidates[x, y] = -99
    if 1 in candidates:
        print(candidates)
    return count

def main(argv=sys.argv):
    verbose = False
    if "-v" in argv:
        verbose = True
    f = argv[-1]

    astromap = [line.strip() for line in open(f,'r').readlines()]
    width = len(astromap[0])
    height = len(astromap)
    placemap = numpy.zeros([height,width], dtype=int)
    countmap = numpy.zeros([height,width], dtype=int)
    pprint(astromap, width=width)
    for x in range(height):
        for y in range(width):
            if astromap[x][y] == '#':
                placemap[x,y] = 1
    print(placemap)
    for x in range(height):
        for y in range(width):
            if placemap[x,y]:
                countmap[x,y] = count(placemap, x, y)
    print(countmap)
    print(numpy.amax(countmap))

if __name__ == "__main__":
    main()
