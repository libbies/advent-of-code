#!/usr/bin/env python3
"""advent of code 2024 day 11 part 2"""
from functools import cache

@cache
def count(stones, depth):
    if depth>=1:
        total = 0
        for stone in stones:
            if stone==0:
                total += count((1,), depth-1)
            elif len(s := str(stone))%2==0:
                total += count((int(s[:len(s)//2]), int(s[len(s)//2:])), depth-1)
            else:
                total += count((stone*2024,), depth-1)
        return total
    return len(stones)

answer = count(tuple(int(_) for _ in open("input.txt").read().split()), 75)
print(count.cache_info())
print("aoc 2024 day 11 part 2:", answer)
