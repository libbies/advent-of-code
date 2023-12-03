#!/usr/bin/env python
"""advent of code 2018 day 9 part 1"""
num_players, last_marble = next(map(int, _.split()[0:7:6]) for _ in open("input.txt").read().splitlines())

scores = {player:0 for player in range(num_players)}
circle = [0]
index = 0
marble = 0
for p in (n%num_players for n in range(last_marble)):
    marble += 1
    if marble%23==0:
        index = (index-7) % len(circle)
        scores[p] += marble + circle.pop(index)
    else:
        index = (index+2) % len(circle)
        circle.insert(index, marble)

answer = max(scores.values())
print("aoc 2018 day 9 part 1:", answer)
