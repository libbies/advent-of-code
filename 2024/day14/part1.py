#!/usr/bin/env python3
"""advent of code 2024 day 14 part 1"""
import re

lines = open("input.txt").read().splitlines()
robots = list()
for line in lines:
    robots.append([int(_) for _ in re.findall(r"[-0-9]+", line)])

height = 103
width = 101
for n in range(100):
    for robot in robots:
        robot[0] = (robot[0]+robot[2])%width
        robot[1] = (robot[1]+robot[3])%height

q0 = sum(1 for x,y,_,_ in robots if x<width//2   and y<height//2  )
q1 = sum(1 for x,y,_,_ in robots if   width//2<x and y<height//2  )
q2 = sum(1 for x,y,_,_ in robots if x<width//2   and   height//2<y)
q3 = sum(1 for x,y,_,_ in robots if   width//2<x and   height//2<y)

answer = q0*q1*q2*q3
print("aoc 2024 day 14 part 1:", answer)
