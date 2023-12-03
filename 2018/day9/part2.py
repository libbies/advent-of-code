#!/usr/bin/env python
"""advent of code 2018 day 9 part 2"""
from collections import deque
num_players, last_marble = next(map(int, _.split()[0:7:6]) for _ in open("input.txt").read().splitlines())

last_marble *= 100

scores = {player:0 for player in range(num_players)}
circle = deque([0])
index = 0
marble = 0
for p in (n%num_players for n in range(last_marble)):
    marble += 1
    if marble%23==0:
        circle.rotate(-7)
        scores[p] += marble + circle.pop()
    else:
        circle.rotate(2)
        circle.append(marble)

answer = max(scores.values())
print("aoc 2018 day 9 part 2:", answer)
