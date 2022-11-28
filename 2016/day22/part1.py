lines = [l.split() for l in open("input.txt").read().splitlines() if "/" in l]

nodes = dict()
for l in lines:
    _, x, y = [s[1:] for s in l[0].split('-')]
    nodes[(int(x), int(y))] = [int(s[:-1]) for s in l[1:]]

candidates=list()
# Filesystem              Size  Used  Avail  Use%
SIZE = 0
USED = 1
AVAIL = 2
PERCENT = 3
for A in nodes:
    if nodes[A][USED] == 0:
        continue
    for B in (n for n in nodes if n!=A):
        if nodes[A][USED] <= nodes[B][AVAIL]:
            candidates.append((A,B))

print("part1:", len(candidates))
