#!/usr/bin/env python
"""advent of code 2023 day 17 part 1"""
import heapq
from collections import defaultdict
lines = [[int(_) for _ in line.strip()] for line in open("input.txt").readlines()]

maxlen = len(lines)
heatmap = dict()
for row, line in enumerate(lines):
    for col, heat in enumerate(line):
        heatmap[row,col] = heat

distances = defaultdict(lambda: float('inf'))

directions = {
    "D": (1, 0), "U": (-1, 0),
    "R": (0, 1), "L": (0, -1),
}

reverse = {
    "D": "U", "U": "D",
    "R": "L", "L": "R",
}

queue = [
    (0, 0, 0, ""),
]

answer = float('inf')
while queue:
    distance, row, col, path = heapq.heappop(queue)
    if row==maxlen-1 and col==maxlen-1:
        answer = min(answer, distance)
    for direction, (dx, dy) in directions.items():
        if path and reverse[path[-1]]==direction:
            continue
        if path.count(direction)==3:
            continue
        r, c, p = row+dx, col+dy, (path+direction)[-3:]
        if 0<=r<maxlen and 0<=c<maxlen:
            if distance + heatmap[r,c] < distances[r,c,p]:
                distances[r,c,p] = distance + heatmap[r,c]
                heapq.heappush(queue, (distances[r,c,p], r, c, p))

print("aoc 2023 day 17 part 1:", answer)
