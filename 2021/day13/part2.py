#!python
"""advent of code 2021 day 13 part 2"""
lines = open("input.txt").read().splitlines()
coords = [[int(c) for c in l.split(',')] for l in lines if ',' in l]
folds = [l.split(' ')[-1] for l in lines if '=' in l]
grid = { x: dict() for x,y in coords }

for x,y in coords:
    grid[x][y] = True

for fold in folds:
    d, line = fold.split('=')
    line = int(line)
    cuts, pastes = list(), list()
    if d=="x": # left
        for x, row in ((x,row) for x,row in grid.items() if x>=line):
            for y, c in row.items():
                cuts.append((x,y))
                pastes.append((line-(x-line),y))
    if d=="y": # right
        for x, row in grid.items():
            for y, c in ((y,c) for y,c in row.items() if y>=line):
                cuts.append((x,y))
                pastes.append((x,line-(y-line)))
    for x,y in cuts:
        del grid[x][y]
    for x,y in pastes:
        if x not in grid:
            grid[x] = dict()
        grid[x][y] = True

coords = list()
for x, row in grid.items():
    for y, c in row.items():
        if grid[x][y]:
            coords.append((x,y))

w = max(c[0] for c in coords)
h = max(c[1] for c in coords)

printout = list()
for _ in range(h+1):
    printout.append(list(' '*(w+1)))

for x,y in coords:
    printout[y][x] = '█'

print("aoc 2021 day 13 part 2:")
for p in printout:
    print(''.join(p))
