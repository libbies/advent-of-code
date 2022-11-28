import numpy

inputs = [s.rsplit(maxsplit=3) for s in open("input.txt").read().splitlines()]

grid = numpy.zeros((1000,1000), dtype=int)
for i in inputs:
    n = [*map(int, i[1].split(','))]
    m = [*map(int, i[3].split(','))]
    if i[0] == "turn on":
        grid[n[0]:m[0]+1,n[1]:m[1]+1] = 1
    elif i[0] == "turn off":
        grid[n[0]:m[0]+1,n[1]:m[1]+1] = 0
    elif i[0] == "toggle":
        for x in range(n[0], m[0]+1):
            for y in range(n[1], m[1]+1):
                if grid[x,y] == 1:
                    grid[x,y] = 0
                elif grid[x,y] == 0:
                    grid[x,y] = 1
    else:
        raise StopIteration

print("part1:", grid.sum())

grid = numpy.zeros((1000,1000), dtype=int)
for i in inputs:
    n = [*map(int, i[1].split(','))]
    m = [*map(int, i[3].split(','))]
    if i[0] == "turn on":
        grid[n[0]:m[0]+1,n[1]:m[1]+1] += 1
    elif i[0] == "turn off":
        for x in range(n[0], m[0]+1):
            for y in range(n[1], m[1]+1):
                grid[x,y] = max(0, grid[x,y]-1)
    elif i[0] == "toggle":
        grid[n[0]:m[0]+1,n[1]:m[1]+1] += 2
    else:
        raise StopIteration

print("part2:", grid.sum())
