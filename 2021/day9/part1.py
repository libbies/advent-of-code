"""advent of code 2021 day 9 part 1"""
import code
from pprint import pprint

heightmap = [
    [int(h) for h in list(l)]
    for l in open("input.txt").read().splitlines()
]

lh = len(heightmap)
lw = len(heightmap[0])

answer = 0
for i, row in enumerate(heightmap):
    for j, c in enumerate(row):
        if i>0 and heightmap[i][j]>=heightmap[i-1][j]:
            continue
        if i<lh-1 and heightmap[i][j]>=heightmap[i+1][j]:
            continue
        if j>0 and heightmap[i][j]>=heightmap[i][j-1]:
            continue
        if j<lw-1 and heightmap[i][j]>=heightmap[i][j+1]:
            continue
        # print(f"low point=heightmap[{i}][{j}], risk={heightmap[i][j]+1}")
        answer += heightmap[i][j] + 1


print("part 1 answer:", answer)
