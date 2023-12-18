#!/usr/bin/env python
"""advent of code 2023 day 12 part 2"""
from functools import cache
lines = [l.split() for l in open("input.txt").readlines()]

@cache
def recurse(springs, found, pending, damaged):
    if '#' in springs and not (damaged or pending):
        # still damaged springs left, but no more groups left to fill
        return 0
    if not springs and (damaged or pending):
        # still groups left but out of springs
        return 0
    if not damaged and not pending:
        # complete!
        return 1
    if springs[0]=='#' and pending > 0:
        # proceed with a group of springs
        return recurse(springs[1:], found+1, pending-1, damaged)
    if springs[0]=='#' and found and not pending:
        # started a group, but too many found
        return 0
    if springs[0]=='.' and not found:
        # ignore '.' if we haven't started a new group yet
        return recurse(springs[1:], 0, pending, damaged)
    if springs[0]=='.' and found and not pending:
        # complete group of springs
        return recurse(springs[1:], 0, damaged[0], damaged[1:])
    if springs[0]=='.' and found and pending:
        # incomplete, invalid
        return 0
    if springs[0]=='?':
        # ¿por que no los dos?
        return (recurse('#' + springs[1:], found, pending, damaged)
              + recurse('.' + springs[1:], found, pending, damaged)
        )

answer = 0
for springs, damaged in lines:
    damaged = tuple(map(int, ','.join([damaged] * 5).split(',')))
    springs = ('?'.join([springs] * 5)).replace("..", '.').strip('.')
    answer += recurse(springs, 0, damaged[0], damaged[1:])

print(recurse.cache_info())
print("aoc 2023 day 12 part 2:", answer)
