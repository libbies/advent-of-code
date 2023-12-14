#!/usr/bin/env python
"""advent of code 2023 day 14 part 1"""
from collections import deque
lines = [list(l.strip()) for l in open("input.txt").readlines()]

for col in range(len(lines)):
    empty = deque()
    for row in range(len(lines)):
        if lines[row][col] == '.':
            empty.append(row)
        elif lines[row][col] == '#':
            empty = deque()
        elif lines[row][col] == 'O' and empty:
            lines[empty.popleft()][col] = 'O'
            lines[row][col] = '.'
            empty.append(row)

answer = 0
for i, row in enumerate(lines):
    answer += row.count('O') * (len(lines) - i)

print("aoc 2023 day 14 part 1:", answer)
