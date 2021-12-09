# from pprint import pprint

rows = [' '+r+' ' for r in open("input.txt").read().replace('.',' ').splitlines()]
rows = [' '*len(rows[0])] + rows + [' '*len(rows[0])]
rows = [[c for c in r] for r in rows]

lr, lc, l = len(rows), len(rows[0]), max(len(rows), len(rows[0]))
iterations = 0
while True:
    # print(iterations)
    state = [r.copy() for r in rows]
    for x in range(1, len(rows)-1):
        for y in range(1, len(rows[0])-1):
            up = (rows[x-n][y] for n in range(1,  x+1) if rows[x-n][y]!=' ')
            dn = (rows[x+n][y] for n in range(1, lr-x) if rows[x+n][y]!=' ')
            ll = (rows[x][y-n] for n in range(1,  y+1) if rows[x][y-n]!=' ')
            rr = (rows[x][y+n] for n in range(1, lc-y) if rows[x][y+n]!=' ')
            ul = (rows[x-n][y-n] for n in range(1, l) if x-n > 0 if y-n > 0 if rows[x-n][y-n]!=' ')
            ur = (rows[x-n][y+n] for n in range(1, l) if x-n > 0 if y+n <lc if rows[x-n][y+n]!=' ')
            dl = (rows[x+n][y-n] for n in range(1, l) if x+n <lr if y-n > 0 if rows[x+n][y-n]!=' ')
            dr = (rows[x+n][y+n] for n in range(1, l) if x+n <lr if y+n <lc if rows[x+n][y+n]!=' ')
            cells = [next(up, None), next(dn, None), next(ll, None), next(rr, None),
                     next(ul, None), next(ur, None), next(dl, None), next(dr, None)]
            if rows[x][y] == 'L' and '#' not in cells:
                state[x][y] = '#'
            if rows[x][y] == '#' and cells.count('#') >= 5:
                state[x][y] = 'L'
    else:
        if state == rows:
            break
        rows = state
        iterations += 1

print(iterations, "iterations, part1:", ''.join([''.join([c for c in r if c=='#']) for r in rows]).count('#'))
