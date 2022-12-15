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

sensors.sort(key=lambda x:-x[-1])
def check(x, y):
    if not (0 < x < 4_000_000) or not (0 < y < 4_000_000):
        return False
    for dx, dy, distance in sensors:
        if abs(dx - x) + abs(dy - y) < distance:
            return False
    return True

answer = 0
for sx, sy, dist in reversed(sensors):
    dist = dist + 1
    for d in range(dist):
        if check(sx+d, sy+dist-d):
            answer = (sx+d) * 4_000_000 + (sy+dist-d)
            break
        if check(sx+d, sy-dist+d):
            answer = (sx+d) * 4_000_000 + (sy-dist+d)
            break
        if check(sx-d, sy-dist+d):
            answer = (sx-d) * 4_000_000 + (sy-dist+d)
            break
        if check(sx-d, sy+dist-d):
            answer = (sx-d) * 4_000_000 + (sy+dist-d)
            break
    if answer:
        break

print("part 2:", answer)
