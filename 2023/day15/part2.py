#!/usr/bin/env python
"""advent of code 2023 day 15 part 2"""
steps = open("input.txt").read().strip().split(',')

def get_hash(label):
    value = 0
    for c in label:
        value = (value + ord(c)) * 17 % 256
    return value

boxes = [[] for _ in range(256)]
for step in steps:
    if '=' in step:
        label, length = step.split('=')
        box = get_hash(label)
        for lens in boxes[box]:
            if lens[0]==label:
                lens[-1] = length
                break
        else:
            boxes[box].append([label, length])
    elif '-' in step:
        label = step.strip('-')
        box = get_hash(label)
        for i, lens in enumerate(boxes[box]):
            if lens[0]==label:
                boxes[box].pop(i)

answer = 0
for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        answer += (i+1) * (j+1) * int(lens[-1])

print("aoc 2023 day 15 part 2:", answer)
