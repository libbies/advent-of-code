"""advent of code 2021 day 9 part 2"""

heightmap = [
    [int(h) for h in list(l)]
    for l in open("input.txt").read().splitlines()
]

lh = len(heightmap)
lw = len(heightmap[0])

basins = dict()
d = dict()
for i, row in enumerate(heightmap):
    for j, c in enumerate(row):
        if heightmap[i][j]==9:
            continue
        # lookup for the point itself or their adjacent neighbor
        lookup = [(k,l) for k,l in ((i,j), (i,j+1)) if (k,l) in d]
        if lookup:
            x, y = d[lookup[0]]
            # if any of the neighbours have a different basin id, merge them
            for basin in lookup[1:]:
                if d[basin]==(x,y):
                    continue
                basins[(x,y)].update(basins[d[basin]])
                d[basin] = (x,y)
        else:
            # no lookup result means new basin
            x, y = i, j
            basins[(x,y)] = {(i,j)}
        # add neighbors
        basins[(x,y)].update({(k,l)
                                for k,l in ((i,j), (i+1,j), (i,j+1))
                                if 0<=k<lh and 0<=l<lw and heightmap[k][l]!=9})
        # add neighbors to the directory for future lookups
        for k, l in ((i+1,j), (i,j+1)):
            if not(0<=k<lh and 0<=l<lw) or heightmap[k][l]==9:
                continue
            d[(k,l)] = (x,y)

largest = sorted(len(g) for g in basins.values())[:-4:-1]
answer = largest[0] * largest[1] * largest[2]

print("day 9 part 2 answer:", answer)
