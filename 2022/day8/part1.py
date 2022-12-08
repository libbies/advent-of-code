#!python
"""advent of code 2022 day 8 part 1"""
trees = [list(map(int, line)) for line in open("input.txt").read().splitlines()]
length = len(trees)
seen = set()

for y in range(length): # left to right of top edge
    tree = -1
    for x in range(length): # top edge looking down
        if trees[x][y] > tree:
            seen.add((x,y))
            tree = trees[x][y]

for y in range(length): # left to right of bottom edge
    tree = -1
    for x in range(length-1, 0, -1): # bottom edge looking up
        if trees[x][y] > tree:
            seen.add((x,y))
            tree = trees[x][y]

for x in range(length): # up to down of left edge
    tree = -1
    for y in range(length): # left edge looking right
        if trees[x][y] > tree:
            seen.add((x,y))
            tree = trees[x][y]

for x in range(length): # up to down of right edge
    tree = -1
    for y in range(length-1, 0, -1): # right edge looking left
        if trees[x][y] > tree:
            seen.add((x,y))
            tree = trees[x][y]

answer = len(seen)
print("part 1:", answer)
