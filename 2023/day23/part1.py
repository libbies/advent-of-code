#!/usr/bin/env python
"""advent of code 2023 day 23 part 1"""
from collections import deque
grid = [list(l.strip()) for l in open("input.txt").readlines()]

length = len(grid)

directions = {
    'v': (1, 0), '^': (-1, 0),
    '>': (0, 1), '<': (0, -1),
}

row, col = (0, grid[0].index('.'))
counts = [[0]*length for _ in range(length)]
counts[row][col] = -1
queue = deque()
queue.append((1, row+1, col, 'v'))
answer = 0
while queue:
    step, row, col, prev = queue.popleft()
    for direction, (dx, dy) in directions.items():
        if not (0<row+dx<length and 0<col+dy<length):
            continue
        if grid[row+dx][col+dy]=='#':
            continue
        if (       prev=='v' and direction=='^'
                or prev=='^' and direction=='v'
                or prev=='<' and direction=='>'
                or prev=='>' and direction=='<'):
            continue
        if (       direction == 'v' and grid[row+dx][col+dy]=='^'
                or direction == '^' and grid[row+dx][col+dy]=='v'
                or direction == '<' and grid[row+dx][col+dy]=='>'
                or direction == '>' and grid[row+dx][col+dy]=='<'):
            continue
        if counts[row+dx][col+dy] >= step:
            continue
        counts[row+dx][col+dy] = step
        queue.append((step+1, row+dx, col+dy, direction))
    answer = max(answer, step)

print("aoc 2023 day 23 part 1:", answer)
