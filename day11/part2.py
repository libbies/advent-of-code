from pprint import pprint
from copy import deepcopy

rows = [' '+r+' ' for r in open("example.txt").read().replace('.',' ').splitlines()]
rows = [' '*len(rows[0])] + rows + [' '*len(rows[0])]
rows = [[c for c in r] for r in rows]
# pprint([''.join(r) for r in rows])

l = max(len(rows), len(rows[0]))
iterations = 0
while True:
    state = deepcopy(rows)
    for x in range(1, len(rows)-1):
        for y in range(1, len(rows[0])-1):
            up = [rows[x-n][y] for n in range(1, x) if 0<x-n<x if rows[x-n][y]!=' ']
            down = [rows[x+n][y] for n in range(1, len(rows)-x) if x+n<len(rows) if rows[x+n][y]!=' ']
            left = [rows[x][y-n] for n in range(1, y) if 0<y-n<y if rows[x][y-n]!=' ']
            right = [rows[x][y+n] for n in range(1, len(rows[0])-y) if y+n<len(rows[0]) if rows[x][y+n]!=' ']
            ul = [rows[x-n][y-n] for n in range(1, max(x, y)) if 0<x-n<x if 0<y-n<y if rows[x-n][y-n]!=' ']
            ur = [rows[x-n][y+n] for n in range(1, max(x, len(rows[0])-y)) if 0<x-n<x if y+n<len(rows[0]) if rows[x-n][y+n]!=' ']
            dl = [rows[x+n][y-n] for n in range(1, max(len(rows)-x, y)) if 0<y-n<y if x+n<len(rows) if rows[x+n][y-n]!=' ']
            dr = [rows[x+n][y+n] for n in range(1, max(len(rows)-x, len(rows[0])-y)) if x+n<len(rows) if y+n<len(rows[0]) if rows[x+n][y+n]!=' ']
            cells = [c[0] for c in [up, down, left, right, ul, ur, dl, dr] if c]
            if rows[x][y] == 'L' and '#' not in cells:
                state[x][y] = '#'
            if rows[x][y] == '#' and cells.count('#') >= 5:
                state[x][y] = 'L'
    else:
        if state == rows:
            break
        rows = state
        iterations += 1
    # pprint([''.join(r) for r in rows])

print(f"{iterations} iterations, part1:", ''.join([''.join([c for c in r if c=='#']) for r in rows]).count('#'))
