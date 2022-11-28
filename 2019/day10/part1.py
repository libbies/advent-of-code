#!/usr/bin/env python3
import sys
import numpy
from pprint import pprint

# https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

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
    candidates[x, y] = -999
    # x:0->x, y:0->y
    for _x in range(x):
        for _y in range(y):
            if candidates[_x, _y] == 1:
                count += 1
                candidates[_x, _y] = -30
                div = gcd(x-_x, y-_y)
                dx, dy = (x-_x)//div, (y-_y)//div
                for n in range(max(h,w)):
                    if n*dx+_x >= x or n*dy+_y >= y:
                        continue
                    if candidates[n*dx+_x, n*dy+_y] > 0:
                        candidates[n*dx+_x, n*dy+_y] = -3
    # x:0->x, y:y->w
    for _x in range(x):
        for _y in range(w-1, y, -1):
            if candidates[_x, _y] == 1:
                count += 1
                candidates[_x, _y] = -40
                div = gcd(x-_x, _y-y)
                dx, dy = (x-_x)//div, (_y-y)//div
                for n in range(max(h,w)):
                    if n*dx+_x >= x or 0>= _y-(n*dy) or _y-(n*dy) >= w:
                        continue
                    if candidates[n*dx+_x, _y-(n*dy)] > 0:
                        candidates[n*dx+_x, -y-(n*dy)] = -4
    # x:x->h, y:0->y
    for _x in range(h-1, x, -1):
        for _y in range(y):
            if candidates[_x, _y] == 1:
                count += 1
                candidates[_x, _y] = -50
                div = gcd(_x-x, y-_y)
                dx, dy = (_x-x)//div, (y-_y)//div
                for n in range(max(h,w)):
                    if 0>= _x-(n*dx) or _x-(n*dx) >= h or n*dy+_y >= y:
                        continue
                    if candidates[_x-(n*dx), n*dy+_y] > 0:
                        candidates[-x-(n*dx), n*dy+_y] = -5
    # x:x->h, y:y->h
    for _x in range(h-1, x, -1):
        for _y in range(w-1, y, -1):
            if candidates[_x, _y] == 1:
                count += 1
                candidates[_x, _y] = -60
                div = gcd(_x-x,_y-y)
                dx, dy = (_x-x)//div, (_y-y)//div
                for n in range(max(h,w)):
                    if 0 >= _x-(n*dx) or _x-(n*dx) >= h or 0 >= _y-(n*dy) or _y-(n*dy) >= w:
                        continue
                    if candidates[_x-(n*dx), _y-(n*dy)] > 0:
                        candidates[_x-(n*dx), _y-(n*dy)] = -6
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
