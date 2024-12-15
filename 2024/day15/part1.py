#!/usr/bin/env python3
"""advent of code 2024 day 15 part 1"""
from collections import defaultdict

lines = open("input.txt").read().split('\n\n')

height = len(lines[0].split())
width = len(lines[0].split()[0])

def pprint():
    for px in range(height):
        for py in range(width):
            if (px,py) == location:
                print('@', end="")
            elif warehouse[px,py]:
                if (px,py) in bounds:
                    print('█', end="")
                else:
                    print(warehouse[px,py], end="")
            else:
                print(' ', end="")
        print()

warehouse = defaultdict(str)
bounds = set()
for x, line in enumerate(lines[0].split()):
    for y, char in enumerate(line):
        if char=='.':
            continue
        if char=='@':
            location = (x,y)
            continue
        if char=='#':
            bounds.add((x,y))
        warehouse[x,y] = char

for move in lines[1].strip():
    x, y = location
    if move in "><":
        d = 1 if move=='>' else -1
        if not warehouse[x,y+d]:
            location = x,y+d
        elif warehouse[x,y+d]=='O':
            for n in range(1, width):
                if (x,y+n*d) in bounds:
                    break
                if not warehouse[x,y+d+n*d]:
                    warehouse[x,y+d+n*d] = 'O'
                    warehouse[location := (x,y+d)] = None
                    break
    if move in "^v":
        d = 1 if move=='v' else -1
        if not warehouse[x+d,y]:
            location = x+d,y
        if warehouse[x+d,y]=='O':
            for n in range(1, height):
                if (x+n*d,y) in bounds:
                    break
                if not warehouse[x+d+n*d,y]:
                    warehouse[x+d+n*d,y] = 'O'
                    warehouse[location := (x+d,y)] = None
                    break

pprint()
answer = 0
for x, y in {k for k in warehouse if warehouse[k]=='O'}:
    answer += 100 * x + y

print("aoc 2024 day 15 part 1:", answer)
