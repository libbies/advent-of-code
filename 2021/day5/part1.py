"""advent of code 2021 day 5 part 1"""
from collections import defaultdict
inputs = (_.split() for _ in open("input.txt").readlines())

points = defaultdict(int)
for p1, _, p2 in inputs:
    x1, y1 = (int(_) for _ in p1.split(','))
    x2, y2 = (int(_) for _ in p2.split(','))
    if x1==x2:
        for point in ((x1, y) for y in range(min(y1, y2), max(y1, y2)+1)):
            points[point] += 1
    if y1==y2:
        for point in ((x, y1) for x in range(min(x1, x2), max(x1, x2)+1)):
            points[point] += 1

answer = sum(1 for count in points.values() if count>=2)
print("part 1 answer:", answer)
