#!python
"""advent of code 2022 day 15 part 1"""
import re
lines = [
    tuple(int(_) for _ in re.findall("[0-9-]+", line))
    for line in open("input.txt").read().splitlines()
]

beacons = set()
for _, _, bx, by in lines:
    beacons.add((bx, by))

positions = list()

target = 2_000_000
for line in lines:
    sx, sy, bx, by = line
    distance = abs(sx - bx) + abs(sy - by)
    height = abs(sy - target)
    if height > distance:
        continue
    positions.append((sx-distance+height, sx+distance-height))

left = min(_[0] for _ in positions)
right = max(_[1] for _ in positions)

row = [0 for _ in range(left, right+1)]
for l, r in positions:
    row[l+abs(left):r+abs(left)+1] = [1 for _ in range(l, r+1)]

answer = sum(row) - sum(1 for b in beacons if b[-1]==2000000)

print("part 1:", answer)
