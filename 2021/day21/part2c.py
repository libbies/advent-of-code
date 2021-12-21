#!python
"""advent of code 2021 day 21 part 1"""
from functools import cache, lru_cache
from itertools import product
p1pos, p2pos = [int(l.split()[-1]) for l in open("input.txt").read().splitlines()]
initial_state = (p1pos, p2pos, 0, 0)
board = [*range(1,11)]

@lru_cache(maxsize=None)
def player1(p1pos, p2pos, p1score, p2score):
    # print("p1", player1.cache_info())
    score = [0, 0]
    for dice in product((1,2,3), (1,2,3), (1,2,3)):
        roll = sum(dice)
        if p1score + board[(p1pos+roll)%10-1]>=21:
            score[0] += 1
        else:
            score = [sum(scores) for scores in zip(score,
                player2(board[(p1pos+roll)%10-1],
                        p2pos,
                        p1score + board[(p1pos+roll)%10-1],
                        p2score))]
    return score

@lru_cache(maxsize=None)
def player2(p1pos, p2pos, p1score, p2score):
    # print("p2", player2.cache_info())
    score = [0, 0]
    for dice in product((1,2,3), (1,2,3), (1,2,3)):
        roll = sum(dice)
        if p2score + board[(p2pos+roll)%10-1] >=21:
            score[1] += 1
        else:
            score = [sum(scores) for scores in zip(score,
                player1(p1pos,
                        board[(p2pos+roll)%10-1],
                        p1score,
                        p2score + board[(p2pos+roll)%10-1]))]

    return score

wins = player1(*initial_state)
print("p1", player1.cache_info())
print("p2", player2.cache_info())
print("aoc 2021 day 21 part 2:", wins)
