from pprint import pprint
from collections import defaultdict

grid = defaultdict(lambda: '.')
for x, row in enumerate(open("input.txt").read().splitlines()):
    for y, cell in enumerate(row):
        grid[(x,y)] = cell

l = len(row)

grid[(0, 0)] = grid[(0, l-1)] = grid[(l-1, 0)] = grid[(l-1, l-1)] = '#'

for n in range(100):
    state = grid.copy()
    for x in range(l):
        for y in range(l):
            if (x, y) in ((0, 0), (0, l-1), (l-1, 0), (l-1, l-1)):
                continue
            alive = [grid[(x+r,y+c)] for r in (-1, 0, 1) for c in (-1, 0, 1)].count('#')
            if grid[(x,y)] == '#' and alive not in (3, 4):
                state[(x,y)] = '.'
            elif grid[(x,y)] == '.' and alive == 3:
                state[(x,y)] = '#'
    if (n+1)%10==0:
        print(n+1, sum(1 for c in grid.values() if c=='#'), '-->', sum(1 for c in state.values() if c=='#'))
    grid = state

print("part1:", sum(1 for c in grid.values() if c=='#'))
