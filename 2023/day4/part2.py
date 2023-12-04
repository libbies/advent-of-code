#!/usr/bin/env python
"""advent of code 2023 day 4 part 2"""
import re
lines = [re.split(r"( \| |: )", l) for l in open("input.txt").read().splitlines()]

class Card:
    pass

cards = dict()
for c, _, numbers, _, winners in lines:
    cid = int(c.split()[-1])
    cards[cid] = Card()
    cards[cid].cid = cid
    cards[cid].points = sum(
        1 for c in [int(_) for _ in numbers.split()]
           if c in [int(_) for _ in winners.split()]
    )
    cards[cid].value = None

max_c = max(cards.keys())
for cid, card in sorted(cards.items(), reverse=True):
    score = 1
    for n in range(cid+1, min(max_c+1, cid+card.points+1)):
        score += cards[n].value
    card.value = score

answer = sum(c.value for c in cards.values())
print("aoc 2023 day 4 part 2:", answer)
