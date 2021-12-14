#!python
"""advent of code 2021 day 13 part 1"""
lines = open("input.txt").read().splitlines()
coords = [[int(_) for _ in l.split(',')] for l in lines if ',' in l]
folds = [l.split(' ')[-1] for l in lines if '=' in l]
w = max(c[0] for c in coords)
h = max(c[1] for c in coords)
grid = { x: dict() for x,y in coords }

for x,y in coords:
    grid[x][y] = True

for fold in folds[:1]:
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

answer = sum(1 for row in grid.values() for c in row.values() if c==True)
print("aoc 2021 day 13 part 1:", answer)
