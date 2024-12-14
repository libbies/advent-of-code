#!/usr/bin/env python3
"""advent of code 2024 day 14 part 1"""
import re

lines = open("input.txt").read().splitlines()
robots = list()
for line in lines:
    robots.append([int(_) for _ in re.findall(r"[-0-9]+", line)])

height = 103
width = 101
def pprint():
    for py in range(height):
        for px in range(width):
            count = sum(1 for r in robots if r[0]==px and r[1]==py)
            print('█' if count else ' ', end="")
        print()

for answer in range(height*width):
    if len({(x,y) for x,y,_,_ in robots})==len(robots):
        pprint()
        break
    for robot in robots:
        robot[0] = (robot[0]+robot[2])%width
        robot[1] = (robot[1]+robot[3])%height

print("aoc 2024 day 14 part 2:", answer)
