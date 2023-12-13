#!/usr/bin/env python
"""advent of code 2023 day 13 part 1"""
grids = (grid.splitlines() for grid in open("input.txt").read().split('\n\n'))

answer = 0
for i, grid in enumerate(grids):
    # horizontal
    for l in range(1,len(grid[0])):
        for row in grid:
            if row[:l][l-len(row):] != row[l:][:l][::-1]:
                # different
                break
        else:
            # found
            answer += l
            break
    # vertical
    for l in range(1, len(grid)):
        for j in range(l):
            if j+l > len(grid)-1:
                continue
            if grid[l-j-1] != grid[l+j]:
                # different
                break
        else:
            # found
            answer += l * 100
            break

print("aoc 2023 day 13 part 1:", answer)
