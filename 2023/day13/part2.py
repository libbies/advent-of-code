#!/usr/bin/env python
"""advent of code 2023 day 13 part 2"""
grids = (grid.splitlines() for grid in open("input.txt").read().split('\n\n'))

answer = 0
for i, grid in enumerate(grids):
    # horizontal
    for l in range(1,len(grid[0])):
        differences = 0
        for row in grid:
            differences += sum(a!=b for a,b in zip(row[:l][l-len(row):], row[l:][:l][::-1]))
            if differences > 1:
                break
        else:
            if differences == 1:
                # found
                answer += l
                break
    # vertical
    for l in range(1, len(grid)):
        differences = 0
        for j in range(l):
            if j+l>len(grid)-1:
                continue
            differences += sum(a!=b for a,b in zip(grid[l-j-1], grid[l+j]))
            if differences > 1:
                break
        else:
            if differences == 1:
                # found
                answer += l * 100

print("aoc 2023 day 13 part 2:", answer)
