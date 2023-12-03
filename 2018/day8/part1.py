#!/usr/bin/env python
"""advent of code 2018 day 8 part 1"""
data = [int(_) for _ in open("input.txt").read().split()][::-1]

stack = []
answer = 0
while stack or data:
    # nothing on stack
    if not stack:
        stack.append([data.pop(), data.pop()])
    # has children
    elif stack[-1][0] > 0:
        stack[-1][0] -= 1
        stack.append([data.pop(), data.pop()])
    # has metadata
    elif stack[-1][0] == 0:
        for n in range(stack[-1][1]):
            answer += data.pop()
        stack.pop()

print("aoc 2018 day 8 part 1:", answer)
