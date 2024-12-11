#!/usr/bin/env python3
"""advent of code 2024 day 11 part 1"""

stones = [int(_) for _ in open("input.txt").read().split()]

for n in range(25):
    tmp = []
    for stone in stones:
        if stone==0:
            tmp.append(1)
        elif len(s := str(stone))%2==0:
            tmp += [ int(s[:len(s)//2]), int(s[len(s)//2:]) ]
        else:
            tmp.append(stone*2024)
    stones = tmp

answer = len(stones)
print("aoc 2024 day 11 part 1:", answer)
