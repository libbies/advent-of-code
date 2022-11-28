"""advent of code 2016 day 24 part 2"""
from itertools import permutations

lines = open("input.txt").read()
numbers = [int(n) for n in lines if n.isdigit()]

grid = dict()
numbers = dict()
for x, line in enumerate(lines.splitlines()):
    for y, c in enumerate(line):
        grid[(x,y)] = c
        if c.isdigit():
            numbers[int(c)]=(x,y)

h, w = list(grid.keys())[-1]

distances = [{n: 0} for n in sorted(numbers)]
for n, location in sorted(numbers.items()):
    start = numbers[n]
    travel = {k: -1 for k,v in grid.items() if v!='#'}
    distance = 0
    distances[n] = {n: 0}
    queue = [location]
    while queue:
        tmp = list()
        for loc in queue:
            if grid[loc].isdigit():
                distances[n][int(grid[loc])] = distance
            travel[loc]=distance
            x, y = loc
            tmp += [loc for loc in ((x-1,y), (x+1,y), (x,y-1), (x,y+1))
                        if loc in travel and travel[loc]==-1 if loc not in tmp]
        queue = tmp
        distance += 1

answer = float("inf")
for p in permutations(range(1,max(numbers)+1)):
    if answer > sum(distances[l][n] for l,n in zip((0,)+p, p+(0,))):
        answer = sum(distances[l][n] for l,n in zip((0,)+p, p+(0,)))

print("aoc 2016 day 24 part 2:", answer)
