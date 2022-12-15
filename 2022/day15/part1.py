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

positions = set()
target = 2_000_000
for sx, sy, bx, by in lines:
    distance = abs(sx - bx) + abs(sy - by)
    dx = abs(sy - target)
    dy = distance - dx
    positions.update(range(sx-dy, sx+dy+1))

answer = len(positions) - sum(1 for b in beacons if b[-1]==target)

print("part 1:", answer)
