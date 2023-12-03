#!/usr/bin/env python
"""advent of code 2023 day 3 part 1"""
lines = [tuple(l) for l in open("input.txt").read().splitlines()]

max_x, max_y = len(lines), len(lines[0])
numbers = dict()
for i, line in enumerate(lines):
    number, coords = "", []
    for j, c in enumerate(line):
        if not number and c.isnumeric():
            number = c
            coords.append((i,j))
        elif number and c.isnumeric():
            number += c
            coords.append((i,j))
        elif number and not c.isnumeric():
            for x, y in coords:
                numbers[x,y] = int(number)
            number, coords = "", []
    if number:
        for x, y in coords:
            numbers[x,y] = int(number)

answer = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '.' or c.isnumeric():
            continue
        if i>0:
            if lines[i-1][j].isnumeric():
                answer += numbers[i-1,j]
            else:
                if j>0 and lines[i-1][j-1].isnumeric():
                    answer += numbers[i-1,j-1]
                if j<max_y and lines[i-1][j+1].isnumeric():
                    answer += numbers[i-1,j+1]
        if i<max_x:
            if lines[i+1][j].isnumeric():
                answer += numbers[i+1,j]
            else:
                if j>0 and lines[i+1][j-1].isnumeric():
                    answer += numbers[i+1,j-1]
                if j<max_y and lines[i+1][j+1].isnumeric():
                    answer += numbers[i+1,j+1]
        if j>0 and line[j-1].isnumeric():
            answer += numbers[i,j-1]
        if j<max_y and line[j+1].isnumeric():
            answer += numbers[i,j+1]

print("aoc 2023 day 3 part 1:", answer)
