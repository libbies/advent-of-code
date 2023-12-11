#!/usr/bin/env python
"""advent of code 2023 day 10 part 2n"""
from collections import deque
lines = open("input.txt").readlines()

class Node(str):
    dist = 0
    up, down, left, right = None, None, None, None

def get_left_edges(node):
    edges = 0
    tmp = node.left
    while tmp:
        if tmp.dist==-1:
            break
        if tmp in ["|", "J", "L", "S"] and tmp.dist>0:
            edges += 1
        tmp = tmp.left
    return edges

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

queue = list()
queue.append(nodes[start[0]][start[-1]])
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
queue = [nodes[0][0]]
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
            answer += get_left_edges(node) % 2

print("aoc 2023 day 10 part 2:", answer)
