#!/usr/bin/env python
"""advent of code 2023 day 7 part 1"""
from collections import Counter, defaultdict
lines = (l.split() for l in open("input.txt").readlines())

translation = {
    65: 'Z', # A
    75: 'Y', # K
    81: 'X', # Q
    74: '0', # J
    84: 'V', # T
}

hands = defaultdict(list)
for hand, bid in lines:
    hand = hand.translate(translation)
    count = Counter(hand)
    if "0" in hand and hand!="00000":
        max_count = max(v for k,v in count.items() if k!="0")
        count = Counter(hand.replace("0",
            sorted(k for k,v in count.items() if v==max_count)[-1]
        ))
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

answer, rank = 0, 0
for hand in ("zero", "one", "two", "three", "full", "four", "five"):
    for _, bid in sorted(hands[hand]):
        rank += 1
        answer += rank * int(bid)

print("aoc 2023 day 7 part 2:", answer)
