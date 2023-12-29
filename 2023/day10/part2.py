#!/usr/bin/env python
"""advent of code 2023 day 10 part 2"""
from collections import deque
lines = open("input.txt").readlines()

class Node(str):
    dist = 0
    up, down, left, right = None, None, None, None

nodes = list()
for row, line in enumerate(lines):
    line = [Node(c) for c in line.strip()]
    for col, node in enumerate(line):
        if node=='S':
            start = node
        if col!=len(line)-1:
            node.right = line[col+1]
        if col!=0:
            node.left = line[col-1]
        if row!=0:
            node.up = nodes[row-1][col]
            nodes[row-1][col].down = node
    nodes.append(line)

queue = deque((start,))
while queue:
    node = queue.pop()
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
        # example2.txt, '7'
        # queue.append(node.left)
        # queue.append(node.down)

node.dist = 1 + max(node.up.dist, node.down.dist, node.left.dist, node.right.dist)

# mark all of the outside
queue = deque((nodes[0][0],))
while queue:
    node = queue.pop()
    if not node.dist:
        node.dist = -1
    if node.up and not node.up.dist:
        queue.append(node.up)
    if node.down and not node.down.dist:
        queue.append(node.down)
    if node.left and not node.left.dist:
        queue.append(node.left)
    if node.right and not node.right.dist:
        queue.append(node.right)

# count edges, odd = inside
answer = 0
for i, row in enumerate(nodes):
    for j, node in enumerate(row):
        if not node.dist:
            edges = 0
            tmp = node.left
            while tmp.dist!=-1:
                if tmp in ["|", "F", "7"] and tmp.dist:
                    edges += 1
                tmp = tmp.left
            answer += edges % 2

print("aoc 2023 day 10 part 2:", answer)
