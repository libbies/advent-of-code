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
                    warehouse[location := (x,y+1)] = None
                    for o in range(1, n+1):
                        warehouse[x,y+o+1] = '[' if o%2==1 else ']'
                    break
    if move=='<':
        if not warehouse[x,y-1]:
            location = x,y-1
        elif warehouse[x,y-1] in "[]":
            for n in range(2, width):
                if (x,y-n) in bounds:
                    break
                if not warehouse[x,y-1-n]:
                    warehouse[location := (x,y-1)] = None
                    for o in range(1, n+1):
                        warehouse[x,y-1-o] = ']' if o%2==1 else '['
                    break
    if move=='v':
        if not warehouse[x+1,y]:
            location = x+1,y
        elif warehouse[x+1,y] in "[]":
            if warehouse[x+1,y] == '[':
                boulders = [(x+1,y), (x+1,y+1)]
            if warehouse[x+1,y] == ']':
                boulders = [(x+1,y), (x+1,y-1)]
            queue = boulders.copy()
            while queue:
                bx, by = queue.pop()
                if (bx+1,by) in bounds:
                    break
                if warehouse[bx+1,by] == '[':
                    queue += [(bx+1,by), (bx+1,by+1)]
                    boulders += queue[-2:]
                elif warehouse[bx+1,by] == ']':
                    queue += [(bx+1,by), (bx+1,by-1)]
                    boulders += queue[-2:]
            else:
                tmp = warehouse.copy()
                for bx, by in reversed(sorted(boulders)):
                    warehouse[bx,by] = None
                    warehouse[bx+1,by] = tmp[bx,by]
                warehouse[location := (x+1,y)] = None
    if move=='^':
        if not warehouse[x-1,y]:
            location = x-1,y
        elif warehouse[x-1,y] in "[]":
            if warehouse[x-1,y] == '[':
                boulders = [(x-1,y), (x-1,y+1)]
            if warehouse[x-1,y] == ']':
                boulders = [(x-1,y), (x-1,y-1)]
            queue = boulders.copy()
            while queue:
                bx, by = queue.pop()
                if (bx-1,by) in bounds:
                    break
                if warehouse[bx-1,by] == '[':
                    queue += [(bx-1,by), (bx-1,by+1)]
                    boulders += queue[-2:]
                elif warehouse[bx-1,by] == ']':
                    queue += [(bx-1,by), (bx-1,by-1)]
                    boulders += queue[-2:]
            else:
                tmp = warehouse.copy()
                for bx, by in sorted(boulders):
                    warehouse[bx,by] = None
                    warehouse[bx-1,by] = tmp[bx,by]
                warehouse[location := (x-1,y)] = None

pprint()
answer = 0
for x, y in {k for k in warehouse if warehouse[k]=='['}:
    answer += 100 * x + y

print("aoc 2024 day 15 part 2:", answer)
