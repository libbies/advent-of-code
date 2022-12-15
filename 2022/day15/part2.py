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

# remove sensors that are completely inside the range of another sensor
sensors.sort(key=lambda x:-x[-1])
for sx, sy, sdist in sensors.copy():
    for tx, ty, tdist in sensors.copy():
        if abs(tx-sx) + abs(ty-sy) < tdist and tdist > 2*sdist:
            sensors.remove((sx, sy, sdist))
            break

# check if (x, y) is not in the range of any sensor
def check(x, y):
    if not 0 < x < 4_000_000 or not 0 < y < 4_000_000:
        return False
    for dx, dy, dist in sensors:
        if abs(dx - x) + abs(dy - y) < dist:
            return False
    return True

# check all points that are just outside of range from (x,y)
def iterate(x, y, dist):
    dist += 1
    for d in range(dist):
        for dx in (d, -d):
            for dy in (dist-d, -(dist-d)):
                if check(x+dx, y+dy):
                    return (x+dx) * 4_000_000 + (y+dy)
    return 0

for sx, sy, distance in reversed(sensors):
    answer = iterate(sx, sy, distance)
    if answer:
        break

print("part 2:", answer)
