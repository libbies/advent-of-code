#!/usr/bin/env python
"""advent of code 2018 day 8 part 2"""
data = [int(_) for _ in open("input.txt").read().split()][::-1]

next_id = (n for n in range(len(data)))
nodes = []
class Node:
    def __init__(self, num_children, num_metadata, node_id=None):
        self.node_id = node_id or next(next_id)
        self.num_children = num_children
        self.num_metadata = num_metadata
        self.children_id = [] # a list of child IDs, not the children themselves
        self.metadata = []
        nodes.append(self)

    def add_child(self, node_id):
        self.children_id.append(node_id)

    @property
    def children(self):
        return [nodes[n] for n in self.children_id]

    @property
    def score(self):
        if not self.num_children:
            return sum(self.metadata)
        return sum(self.children[n-1].score for n in self.metadata if 0 < n <= self.num_children)

    def __repr__(self):
        return (f"Node(num_children={self.num_children}, "
                     f"num_metadata={self.num_metadata}, "
                     f"node_id={self.node_id})")

stack = []
node = None
while data:
    if stack:
        node = nodes[stack[-1]]
    # nothing on stack
    if not node:
        node = Node(data.pop(), data.pop())
        stack.append(node.node_id)
    # has children
    elif node.num_children > len(node.children):
        child = Node(data.pop(), data.pop())
        node.add_child(child.node_id)
        stack.append(child.node_id)
    # has metadata
    elif node.num_metadata > len(node.metadata):
        for n in range(node.num_metadata):
            node.metadata.append(data.pop())
        stack.pop()

answer = nodes[0].score
print("aoc 2018 day 8 part 2:", answer)
