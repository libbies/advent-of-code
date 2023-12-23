#!/usr/bin/env python
"""advent of code 2023 day 23 part 2"""
from collections import deque, defaultdict
import heapq
grid = [list(l.strip()) for l in open("input.txt").readlines()]

length = len(grid)

directions = {
    'v': (1, 0), '^': (-1, 0),
    '>': (0, 1), '<': (0, -1),
}

start = (0, grid[0].index('.'))
end = (length-1, grid[-1].index('.'))

nodes = {start, end}
for row, line in enumerate(grid):
    for col, c  in enumerate(line):
        if (row, col) in nodes:
            continue
        if c=='#':
            continue
        if sum(grid[row+dx][col+dy]!='#' for dx, dy in directions.values())>2:
            nodes.add((row,col))

graph = defaultdict(set)
queue = deque()
for node in nodes:
    visited = {node}
    queue.append((*node, 0))
    while queue:
        row, col, step = queue.popleft()
        if (row,col) in nodes and (row,col)!=node:
            graph[node].add((row, col, step))
            graph[(row,col)].add((*node, step))
            continue
        if not (0<row<length-1 and 0<col<length-1):
            continue
        for dx,dy in directions.values():
            if grid[row+dx][col+dy]=='#' or (row+dx,col+dy) in visited:
                continue
            visited.add((row+dx, col+dy))
            queue.append((row+dx, col+dy, step+1))

def dfs(graph, start, end, visited=set(), distance=0, answer=0):
    visited.add(start)
    if start==end:
        answer = max(answer, distance)
    else:
        for row, col, step in graph[start]:
            if (row, col) not in visited:
                answer = dfs(graph, (row, col), end, visited, distance+step, answer)
    visited.remove(start)
    return answer

answer = dfs(graph, start, end)
print("aoc 2023 day 23 part 2:", answer)
