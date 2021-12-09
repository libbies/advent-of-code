from pprint import pprint

tiles = dict()
for lines in map(str.split, open("input.txt").read().split('\n\n')):
    # print(tile)
    tiles[lines[1][:-1]] = [
        lines[2],
        ''.join((r[-1] for r in lines[2:])),
        lines[-1],
        ''.join((r[0] for r in lines[2:])),
    ]

answer = 1
for id, tile in tiles.items():
    matches = 0
    for edge in tile:
        match = [k for k, v in tiles.items() if k!=id and edge in v or edge[::-1] in v]
        # print(id, edge, len(match), match)
        matches += len(match)
    if matches == 2:
        answer *= int(id)

print("part1:", answer)
