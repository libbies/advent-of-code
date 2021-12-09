#!/usr/bin/env python3

slope = [*map(str.strip, open("input.txt").readlines())]

trees, y = 0, 0
for x in range(1, len(slope)):
    y += 3
    # print(f"x: {x}, y: {y%len(slope[x])} = {slope[x][y%len(slope[x])]}")
    if slope[x][y%len(slope[x])]=="#":
        trees += 1

print(trees)
