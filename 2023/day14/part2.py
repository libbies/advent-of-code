#!/usr/bin/env python
"""advent of code 2023 day 14 part 2"""
from collections import deque
lines = [list(l.strip()) for l in open("input.txt").readlines()]

length = len(lines)
dirs = ('N', 'W', 'S', 'E')
grids = dict()
empty = deque()
answer, turn = 0, 0
while not answer:
    turn += 1
    direction = dirs[(turn-1)%4]
    if direction in ('N', 'S'):
        for col in range(length):
            empty.clear()
            for row in range(length)[::-1 if direction=='S' else 1]:
                if lines[row][col] == '.':
                    empty.append(row)
                elif lines[row][col] == '#':
                    empty.clear()
                elif lines[row][col] == 'O' and empty:
                    lines[empty.popleft()][col] = 'O'
                    lines[row][col] = '.'
                    empty.append(row)
    if direction in ('W', 'E'):
        for row in range(length):
            empty.clear()
            for col in range(length)[::-1 if direction=='E' else 1]:
                if lines[row][col] == '.':
                    empty.append(col)
                elif lines[row][col] == '#':
                    empty.clear()
                elif lines[row][col] == 'O' and empty:
                    lines[row][empty.popleft()] = 'O'
                    lines[row][col] = '.'
                    empty.append(col)
        if direction == 'E':
            if (grid := ''.join(''.join(l) for l in lines)) in grids:
                if (4_000_000_000 - turn) % (turn - grids[grid]) == 0:
                    for i, row in enumerate(lines):
                        answer += row.count('O') * (length - i)
            grids[grid] = turn

print("aoc 2023 day 14 part 2:", answer)
