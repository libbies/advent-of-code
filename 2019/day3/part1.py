#!/usr/bin/env python3
import sys, numpy

wires = open("input.txt", 'r').readlines()

wires = [i.split(',') for i in wires for i in i.split()]

def dimensions(wire):
    height, hmax, width, wmax = 0, 0, 0, 0
    for path in wire:
        direction = path[0]
        length = int(path[1:])
        if direction == 'D':
            height += length
        elif direction == 'U':
            height -= length
        elif direction == 'R':
            width += length
        elif direction == 'L':
            width -= length
        hmax = max([hmax, height, -1 * height])
        wmax = max([wmax, width, -1 * width])
    return([hmax, wmax])

grid1dim = dimensions(wires[0])
grid2dim = dimensions(wires[1])

height = max(grid1dim[0], grid2dim[0])
width = max(grid1dim[1], grid2dim[1])

# width = sum([int(w[1:]) for w in wires[0] if 'R' in w or 'L' in w])
# height = sum([int(w[1:]) for w in wires[1] if 'U' in w or 'D' in w])

print(f"h: {height*2+1}, w: {width*2+1}")

grid1 = numpy.empty([height*2+3, width*2+3], dtype=int)
grid2 = numpy.empty([height*2+3, width*2+3], dtype=int)


def draw(grid, wire, n):
    x, y = height+1, width+1
    for path in wire:
        direction = path[0]
        length = int(path[1:])
        if direction == 'D':
            grid[x:x+length+1, y] = n # this goes down
            x += length
        elif direction == 'U':
            grid[x-length:x, y] = n # this goes up
            x -= length
        elif direction == 'R':
            grid[x, y:y+length+1] = n # this goes right
            y += length
        elif direction == 'L':
            grid[x, y-length:y] = n # this goes left
            y -= length

draw(grid1, wires[0], 1)
print(f"memory used for grid1: {sys.getsizeof(grid1)}")

draw(grid2, wires[1], 2)
print(f"memory used for grid2: {sys.getsizeof(grid2)}")

grid = grid1 + grid2
print(f"memory used for grid: {sys.getsizeof(grid)}")

# my host runs out of memory lol
del(grid1)
del(grid2)

# the origin should be ignored
grid[height+1, width+1] = -1

# numpy.savetxt("grid.csv", grid, delimiter='', fmt="%1d")

for s in range(height+width):
    for x in range(s):
        y = s - x
        # FIXME: we don't actually need to search the entire segment here
        #        just the first and last items
        segmentD = grid[height+1+x:height+2+x, width+1-y:width+1+y] # search down of origin
        segmentU = grid[height-x:height+1-x, width+1-y:width+1+y] # search up of origin
        segmentR = grid[height+1-y:height+1+y, width+1+x:width+2+x] # search right of origin
        segmentL = grid[height+1-y:height+1+y, width-x:width+1-x] # search left of origin
        if [3 for segment in [ segmentD, segmentU, segmentR, segmentL ] if 3 in segment]:
            print(f"x:{x} + y:{y} = {x+y}")
            raise(StopIteration)
