#!/usr/bin/env python3
"""advent of code 2024 day 15 part 2"""
from collections import defaultdict

lines = open("input.txt").read().split("\n\n")

height = len(lines[0].split())
width = len(lines[0].split()[0]) * 2

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
    offset = 0
    for y, char in enumerate(line):
        if char=='.':
            pass
        if char=='@':
            location = (x,y+offset)
        if char=='#':
            bounds.add((x,y+offset))
            bounds.add((x,y+offset+1))
            warehouse[x,y+offset] = char
            warehouse[x,y+offset+1] = char
        if char=='O':
            warehouse[x,y+offset] = '['
            warehouse[x,y+offset+1] = ']'
        offset += 1

for move in lines[1].strip():
    x, y = location
    if move=='>':
        if not warehouse[x,y+1]:
            location = x,y+1
        elif warehouse[x,y+1] in "[]":
            for n in range(2, width):
                if (x,y+n) in bounds:
                    break
                if not warehouse[x,y+n+1]:
                    for m in range(1, n+1):
                        warehouse[x,y+m+1] = '[' if m%2==1 else ']'
                    warehouse[location := (x,y+1)] = None
                    break
    if move=='<':
        if not warehouse[x,y-1]:
            location = x,y-1
        elif warehouse[x,y-1] in "[]":
            for n in range(2, width):
                if (x,y-n) in bounds:
                    break
                if not warehouse[x,y-1-n]:
                    for m in range(1, n+1):
                        warehouse[x,y-1-m] = ']' if m%2==1 else '['
                    warehouse[location := (x,y-1)] = None
                    break
    if move in "^v":
        d = 1 if move=='v' else -1
        if not warehouse[x+d,y]:
            location = x+d,y
        elif warehouse[x+d,y] in "[]":
            if warehouse[x+d,y] == '[':
                boulders = [(x+d,y), (x+d,y+1)]
            if warehouse[x+d,y] == ']':
                boulders = [(x+d,y), (x+d,y-1)]
            queue = boulders.copy()
            while queue:
                bx, by = queue.pop()
                if (bx+d,by) in bounds:
                    break
                if warehouse[bx+d,by] == '[':
                    queue += [(bx+d,by), (bx+d,by+1)]
                    boulders += queue[-2:]
                elif warehouse[bx+d,by] == ']':
                    queue += [(bx+d,by), (bx+d,by-1)]
                    boulders += queue[-2:]
            else:
                tmp = warehouse.copy()
                boulders = sorted(boulders)
                if move=='v':
                    boulders = reversed(boulders)
                for bx,by in boulders:
                    warehouse[bx,by] = None
                    warehouse[bx+d,by] = tmp[bx,by]
                warehouse[location := (x+d,y)] = None

pprint()
answer = 0
for x, y in {k for k in warehouse if warehouse[k]=='['}:
    answer += 100 * x + y

print("aoc 2024 day 15 part 2:", answer)
