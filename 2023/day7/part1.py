#!/usr/bin/env python
"""advent of code 2023 day 7 part 1"""
from collections import Counter, defaultdict
lines = (l.split() for l in open("input.txt").readlines())

translation = {
    65: 'Z', # A
    75: 'Y', # K
    81: 'X', # Q
    74: 'W', # J
    84: 'V', # T
}

hands = defaultdict(list)
for hand, bid in lines:
    hand = hand.translate(translation)
    count = Counter(hand)
    if 5 in count.values():
        hands["five"].append((hand, bid))
    elif 4 in count.values():
        hands["four"].append((hand, bid))
    elif 3 in count.values() and 2 in count.values():
        hands["full"].append((hand, bid))
    elif 3 in count.values():
        hands["three"].append((hand, bid))
    elif 2 == [*count.values()].count(2):
        hands["two"].append((hand, bid))
    elif 2 in count.values():
        hands["one"].append((hand, bid))
    else:
        hands["zero"].append((hand, bid))

answer, rank = 0, 1
for hand in ("zero", "one", "two", "three", "full", "four", "five"):
    for _, bid in sorted(hands[hand]):
        answer += rank * int(bid)
        rank += 1

print("aoc 2023 day 7 part 1:", answer)
