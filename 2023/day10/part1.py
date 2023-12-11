#!/usr/bin/env python
"""advent of code 2023 day 10 part 1"""
from collections import deque
lines = open("input.txt").readlines()


class Node(str):
    dist = 0
    up, down, left, right = None, None, None, None

nodes = list()
for row, line in enumerate(lines):
    tmp = []
    for pipe in line.strip():
        tmp.append(Node(pipe))
    for col, node in enumerate(tmp):
        if node=='S':
            start = (row, col)
        if col!=len(tmp)-1:
            node.right = tmp[col+1]
        if col!=0:
            node.left = tmp[col-1]
        if row!=0:
            node.up = nodes[row-1][col]
            nodes[row-1][col].down = node
    nodes.append(tmp)

queue = deque()
queue.append(nodes[start[0]][start[-1]])
while queue:
    node = queue.popleft()
    if node=='F':
        if not node.down.dist:
            node.dist = node.right.dist + 1
            queue.append(node.down)
        if not node.right.dist:
            node.dist = node.down.dist + 1
            queue.append(node.right)
    if node=='7':
        if not node.down.dist:
            node.dist = node.left.dist + 1
            queue.append(node.down)
        if not node.left.dist:
            node.dist = node.down.dist + 1
            queue.append(node.left)
    if node=='J':
        if not node.up.dist:
            node.dist = node.left.dist + 1
            queue.append(node.up)
        if not node.left.dist:
            node.dist = node.up.dist + 1
            queue.append(node.left)
    if node=='L':
        if not node.up.dist:
            node.dist = node.right.dist + 1
            queue.append(node.up)
        if not node.right.dist:
            node.dist = node.up.dist + 1
            queue.append(node.right)
    if node=='|':
        if not node.down.dist:
            node.dist = node.up.dist + 1
            queue.append(node.down)
        if not node.up.dist:
            node.dist = node.down.dist + 1
            queue.append(node.up)
    if node=='-':
        if not node.left.dist:
            node.dist = node.right.dist + 1
            queue.append(node.left)
        if not node.right.dist:
            node.dist = node.left.dist + 1
            queue.append(node.right)
    if node=='S': # example2: '7', input: 'J'
        node.dist = 1
        # this is hard coded :|
        # input.txt, 'J'
        queue.append(node.up)
        queue.append(node.left)

# nodes are 1-indexed
node.dist = 1 + max(node.up.dist, node.down.dist, node.left.dist, node.right.dist)
answer = node.dist - 1
print("aoc 2023 day 10 part 1:", answer)
