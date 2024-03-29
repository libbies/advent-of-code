#!/usr/bin/env python
"""advent of code 2023 day 18 part 2"""
from collections import defaultdict
lines = [l.split() for l in open("input.txt").readlines()]

# https://stackoverflow.com/a/5389547
def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)

digs = list()
row, col = 0, 0
dirs = {
    '0': 'R',
    '1': 'D',
    '2': 'L',
    '3': 'U',
}
for _, _, color in lines:
    distance = int('0x' + color[2:7], 16)
    direction = dirs[color[7]]
    if direction == "U":
        digs.append((range(row-distance, row), col))
        row -= distance
    if direction == "D":
        digs.append((range(row, row+distance), col))
        row += distance
    if direction == "L":
        digs.append((range(row, row), range(col-distance, col)))
        col -= distance
    if direction == "R":
        digs.append((range(row, row), range(col, col+distance)))
        col += distance

# every change in rows
rows = sorted({dig[0].start for dig in digs} | {dig[0].stop-1 for dig in digs})

answer = 1 # i do not fully understand why the answer is off by one :(
prev = rows[0]
for n in rows[1:]:
    cols = sorted(dig[1] for dig in digs if n in dig[0] and isinstance(dig[1], int))
    ranges = [dig[1] for dig in digs if n==dig[0].start and isinstance(dig[1], range)]
    distance = sum(b-a+1 for a,b in pairwise(cols))
    for r in ranges:
        if any(a<(r.start+r.stop)//2<b for a,b in pairwise(cols)):
            # if the midpoint of a range is between cols, it is already counted
            continue
        distance += len(r)
    answer += distance*(n-prev) # n-prev == number of identical rows
    prev = n

print("aoc 2023 day 18 part 2:", answer)
