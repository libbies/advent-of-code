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
    distance = int('0x' + color[2:7],16)
    direction = dirs[color[7]]
    if direction == "U":
        digs.append((range(row-distance, row), col))
        row -= distance
    if direction == "D":
        digs.append((range(row, row+distance), col))
        row += distance
    # range(row, row-1) is an awful hack lol
    if direction == "L":
        digs.append((range(row, row-1), range(col-distance, col)))
        col -= distance
    if direction == "R":
        digs.append((range(row, row-1), range(col, col+distance)))
        col += distance

rows = sorted({dig[0].start for dig in digs} | {dig[0].stop for dig in digs})

answer = 1 # i do not fully understand why the answer is off by one :(
prev = rows[0]
for n in rows[1:]:
    distance = 0
    cols = sorted(dig[1] for dig in digs if n in dig[0] if isinstance(dig[1], int))
    ranges = [dig[1] for dig in digs if n==dig[0].start if isinstance(dig[1], range)]
    if not ranges:
        distance = sum(b-a+1 for a,b in pairwise(cols))
    elif not cols:
        distance = sum(len(range) for range in ranges)
    else:
        cols = [range(a,b+1) for a,b in pairwise(cols)]
        for r in ranges:
            if any((r.start+r.stop)//2 in col for col in cols):
                continue
            distance += len(r)
        distance += sum(len(range) for range in cols)
    answer += distance*(n-prev)
    prev = n

print("aoc 2023 day 18 part 2:", answer)
