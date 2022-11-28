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

grid1 = numpy.zeros([height*2+3, width*2+3], dtype=int)
grid2 = numpy.zeros([height*2+3, width*2+3], dtype=int)

def draw(grid, wire):
    x, y, run = height+1, width+1, 0
    for path in wire:
        direction = path[0]
        length = int(path[1:])
        if direction == 'D':
            for l in range(1, length+1):
                grid[x+l, y] = run + l # this goes down
            x += length
        elif direction == 'U':
            for l in range(1, length+1):
                grid[x-l, y] = run + l # this goes up
            x -= length
        elif direction == 'R':
            for l in range(1, length+1):
                grid[x, y+l] = run + l # this goes right
            y += length
        elif direction == 'L':
            for l in range(1, length+1):
                grid[x, y-l] = run + l # this goes left
            y -= length
        run += length

draw(grid1, wires[0])
print(f"memory used for grid1: {sys.getsizeof(grid1)}")

draw(grid2, wires[1])
print(f"memory used for grid2: {sys.getsizeof(grid2)}")

gridA = grid1 + grid2
print(f"memory used for grid: {sys.getsizeof(gridA)}")

gridM = grid1 * grid2
print(f"memory used for grid: {sys.getsizeof(gridM)}")

del(grid1)
del(grid2)

gridmin = numpy.min(gridA[numpy.nonzero(gridM)])
print(gridmin)
