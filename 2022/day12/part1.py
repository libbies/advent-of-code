#!python
"""advent of code 2022 day 12 part 1"""
from collections import defaultdict

hmap = [[*map(ord, line)] for line in open("input.txt").read().splitlines()]
for x, line in enumerate(hmap):
    if ord('S') in line:
        start = (x, line.index(ord('S')), ord('a'))
    if ord('E') in line:
        end = (x, line.index(ord('E')), ord('z'))
        hmap[x][line.index(ord('E'))] = ord('z')

hmap = defaultdict(lambda: defaultdict(lambda:256), {
    x: defaultdict(lambda:256, dict(enumerate(line)))
    for x, line in enumerate(hmap)
})

visited = set()
points = [start]
answer = 0
while end not in points:
    answer += 1
    new = set()
    for x, y, h in points.copy():
        if (x, y, h) in visited:
            continue
        if h+1>=hmap[x+1][y]:
            new.add((x+1, y, hmap[x+1][y]))
        if h+1>=hmap[x][y+1]:
            new.add((x, y+1, hmap[x][y+1]))
        if h+1>=hmap[x-1][y]:
            new.add((x-1, y, hmap[x-1][y]))
        if h+1>=hmap[x][y-1]:
            new.add((x, y-1, hmap[x][y-1]))
        visited.add((x, y, h))
    points = new

print("part 1:", answer)
