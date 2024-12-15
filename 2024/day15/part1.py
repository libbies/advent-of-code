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
    if move=='>':
        if not warehouse[x,y+1]:
            location = x,y+1
        elif warehouse[x,y+1]=='O':
            for n in range(1, width):
                if (x,y+n) in bounds:
                    break
                if not warehouse[x,y+1+n]:
                    location = x,y+1
                    warehouse[location] = None
                    warehouse[x,y+1+n] = 'O'
                    break
    if move=='<':
        if not warehouse[x,y-1]:
            location = x,y-1
        elif warehouse[x,y-1]=='O':
            for n in range(1, width):
                if (x,y-n) in bounds:
                    break
                if not warehouse[x,y-1-n]:
                    location = x,y-1
                    warehouse[location] = None
                    warehouse[x,y-1-n] = 'O'
                    break
    if move=='v':
        if not warehouse[x+1,y]:
            location = x+1,y
        if warehouse[x+1,y]=='O':
            for n in range(1, height):
                if (x+n,y) in bounds:
                    break
                if not warehouse[x+1+n,y]:
                    location = x+1,y
                    warehouse[location] = None
                    warehouse[x+1+n,y] = 'O'
                    break
    if move=='^':
        if not warehouse[x-1,y]:
            location = x-1,y
        if warehouse[x-1,y]=='O':
            for n in range(1, height):
                if (x-n,y) in bounds:
                    break
                if not warehouse[x-1-n,y]:
                    location = x-1,y
                    warehouse[location] = None
                    warehouse[x-1-n,y] = 'O'
                    break

pprint()
answer = 0
for x, y in {k for k in warehouse if warehouse[k]=='O'}:
    score = 100 * x + y
    answer += score

print("aoc 2024 day 15 part 1:", answer)
