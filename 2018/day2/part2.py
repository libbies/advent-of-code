#!/usr/bin/env python
"""advent of code 2018 day 2 part 2"""
lines = open("input.txt").read().splitlines()

l = len(lines[0])
for box1 in lines:
    for box2 in lines:
        if sum(box1[i]==box2[i] for i in range(l)) == l - 1:
            answer = ''.join(box1[i] for i in range(l) if box1[i]==box2[i])
            print("aoc 2018 day 2 part 2:", answer)
            raise SystemExit
