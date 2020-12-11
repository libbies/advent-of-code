from pprint import pprint
from copy import deepcopy

rows = ['.'+r+'.' for r in open("input.txt").read().splitlines()]
rows = ['.'*len(rows[0])] + rows + ['.'*len(rows[0])]
rows = [[c for c in r] for r in rows]
# pprint(rows, width=1000)

while True:
    state = deepcopy(rows)
    for x in range(1, len(rows)-1):
        for y in range(1, len(rows[0])-1):
            # print(rows[x+1][y-1:y+2], len(rows[x+1][y-1:y+2]), len(rows))
            cells = (rows[x][y-1:y+2:2] + rows[x-1][y-1:y+2] + rows[x+1][y-1:y+2])
            # print(x, y, repr(cells), len(cells))
            if rows[x][y] == 'L' and '#' not in cells:
                state[x][y] = '#'
            if rows[x][y] == '#' and cells.count('#') >= 4:
                state[x][y] = 'L'
    # pprint(state, width=1000)
    if state==rows:
        break
    else:
        rows=deepcopy(state)

print("part1:", ''.join([''.join([c for c in r if c=='#']) for r in rows]).count('#'))
