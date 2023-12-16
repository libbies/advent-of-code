#!/usr/bin/env python
"""advent of code 2023 day 16 part 1"""
lines = [list(l.strip()) for l in open("input.txt").readlines()]
maxlen = len(lines)

queue = [(0, -1, "R")]
visited = [[0] * maxlen for _ in range(maxlen)]
history = set()
while queue:
    row, col, direction = queue.pop()
    if (row, col, direction) in history:
        continue
    history.add((row, col, direction))
    if (direction=='R' and col+1<maxlen) or (direction=='L' and col-1>=0):
        n = col+1 if direction=='R' else col-1
        visited[row][n] = 1
        match lines[row][n]:
            case '/':
                queue.append((row, n, 'U' if direction=='R' else 'D'))
            case '\\':
                queue.append((row, n, 'D' if direction=='R' else 'U'))
            case '|':
                queue.append((row, n, 'U' if direction=='R' else 'D'))
                queue.append((row, n, 'D' if direction=='R' else 'U'))
            case _:
                queue.append((row, n, 'R' if direction=='R' else 'L'))
    if (direction=='D' and row+1<maxlen) or (direction=='U' and row-1>=0):
        n = row+1 if direction=='D' else row-1
        visited[n][col] = 1
        match lines[n][col]:
            case '/':
                queue.append((n, col, 'L' if direction=='D' else 'R'))
            case '\\':
                queue.append((n, col, 'R' if direction=='D' else 'L'))
            case '-':
                queue.append((n, col, 'L' if direction=='D' else 'R'))
                queue.append((n, col, 'R' if direction=='D' else 'L'))
            case _:
                queue.append((n, col, 'D' if direction=='D' else 'U'))

answer = sum(sum(row) for row in visited)
print("aoc 2023 day 16 part 1:", answer)








#
