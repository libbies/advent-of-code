#!/usr/bin/env python
"""advent of code 2018 day 13 part 1"""
lines = open("example.txt").read().splitlines()

grid = {(x,y): c for y, row in enumerate(lines) for x, c in enumerate(row)}
max_x = max(_[0] for _ in grid.keys()) + 1
max_y = max(_[1] for _ in grid.keys()) + 1

def pprint():
    print('\n'.join(''.join(grid[x,y] for x in range(max_x)) for y in range(max_y)))

carts = {}
history = {}
for (x,y), c in grid.items():
    if c in ['<', '>']:
        grid[x,y] = "-"
        carts[x,y] = [(x,y), c, history.copy()]
    if c in ['v', '^']:
        grid[x,y] = "|"
        carts[x,y] = [(x,y), c, history.copy()]

tick = 0
while True:




    tick += 1

answer = 0
print("aoc 2018 day 13 part 1:", answer)
