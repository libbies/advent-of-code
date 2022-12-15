#!python
"""advent of code 2022 day 15 part 2"""
import re
lines = [
    tuple(int(_) for _ in re.findall("[0-9-]+", line))
    for line in open("input.txt").read().splitlines()
]

sensors = list()
for sx, sy, bx, by in lines:
    sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))

bound = 4_000_000
sensors.sort(key=lambda x:-x[-1])
def check(x, y):
    if not 0 < x < bound or not 0 < y < bound:
        return False
    for dx, dy, dist in sensors:
        if abs(dx - x) + abs(dy - y) < dist:
            return False
    return True

def iterate(x, y, dist):
    for d in range(dist):
        for dx in (d, -d):
            for dy in (dist-d, -(dist-d)):
                if check(x+dx, y+dy):
                    return (x+dx) * bound + (y+dy)
    return 0

for sx, sy, distance in reversed(sensors):
    answer = iterate(sx, sy, distance+1)
    if answer:
        break

print("part 2:", answer)
