#!python
"""advent of code 2022 day 18 part 1"""
from collections import defaultdict
cubes = [tuple(map(int, line.split(','))) for line in open("input.txt").read().splitlines()]

grid = defaultdict(lambda: 0)
for x, y, z in cubes:
    grid[x,y,z] = 1

answer = 0
for x, y, z in grid.copy():
    surfaces = 6
    for i, j, k in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
        if grid[x+i,y+j,z+k]==1:
            surfaces -= 1
    answer += surfaces

print("part 1:", answer)
