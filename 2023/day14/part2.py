#!/usr/bin/env python
"""advent of code 2023 day 14 part 2"""
from collections import deque

def load(lines):
    l = 0
    for i, row in enumerate(lines):
        l += row.count('O') * (len(lines) - i)
    return l

lines = [list(l.strip()) for l in open("input.txt").readlines()]
grids = dict()
dirs = ('N', 'W', 'S', 'E')
answer = 0
for turn in range(1, 4_000_000_001):
    direction = dirs[(turn-1)%4]
    if direction == 'N':
        for col in range(len(lines[0])):
            empty = deque()
            for row in range(len(lines)):
                if lines[row][col] == '.':
                    empty.append(row)
                if lines[row][col] == '#':
                    empty = deque()
                if lines[row][col] == 'O' and empty:
                    lines[empty.popleft()][col] = 'O'
                    lines[row][col] = '.'
                    empty.append(row)
    if direction=='W':
        for row in range(len(lines)):
            empty = deque()
            for col in range(len(lines[0])):
                if lines[row][col] == '.':
                    empty.append(col)
                if lines[row][col] == '#':
                    empty = deque()
                if lines[row][col] == 'O' and empty:
                    lines[row][empty.popleft()] = 'O'
                    lines[row][col] = '.'
                    empty.append(col)
    if direction == 'S':
        for col in range(len(lines[0])):
            empty = deque()
            for row in reversed(range(len(lines))):
                if lines[row][col] == '.':
                    empty.append(row)
                if lines[row][col] == '#':
                    empty = deque()
                if lines[row][col] == 'O' and empty:
                    lines[empty.popleft()][col] = 'O'
                    lines[row][col] = '.'
                    empty.append(row)
    if direction=='E':
        for row in range(len(lines)):
            empty = deque()
            for col in reversed(range(len(lines[0]))):
                if lines[row][col] == '.':
                    empty.append(col)
                if lines[row][col] == '#':
                    empty = deque()
                if lines[row][col] == 'O' and empty:
                    lines[row][empty.popleft()] = 'O'
                    lines[row][col] = '.'
                    empty.append(col)
        grid = ''.join(''.join(l) for l in lines)
        if grid in grids:
            if (4_000_000_000 - turn) % (turn - grids[grid]) == 0:
                answer = load(lines)
        grids[grid] = turn
    if answer:
        break

print("aoc 2023 day 14 part 2:", answer)
