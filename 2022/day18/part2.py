#!python
"""advent of code 2022 day 18 part 2"""
from collections import defaultdict, Counter
cubes = [tuple(map(int, line.split(','))) for line in open("input.txt").read().splitlines()]

l = max(max(cube) for cube in cubes)

grid = defaultdict(lambda: None)
for x, y, z in cubes:
    grid[x,y,z] = 1

for x, y, z in [(0,0,0), (0,0,l), (0,0,0), (0,l,0), (0,0,0), (l,0,0)]:
    grid[x,y,z] = -1

finished = False
while not finished:
    finished = True
    for (x,y,z), value in grid.copy().items():
        if not (-1<=x<=l+1 and -1<=y<=l+1 and -1<=z<=l+1):
            continue
        if value!=-1:
            continue
        for i, j, k in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
            if not grid[x+i,y+j,z+k]:
                grid[x+i,y+j,z+k]=-1
                finished = False

answer = 0
for (x,y,z), value in grid.copy().items():
    if value!=1:
        continue
    for i, j, k in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
        if grid[x+i,y+j,z+k]==-1:
            answer += 1

print("part 2:", answer)
