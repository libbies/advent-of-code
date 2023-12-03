#!/usr/bin/env python
"""advent of code 2018 day 1 part 2"""
numbers = [int(_) for _ in open("input.txt").read().splitlines()]

frequencies = {0}
freq = 0
answer = None
while not answer:
    for n in numbers:
        freq += n
        if freq in frequencies:
            answer = freq
            break
        frequencies.add(freq)

print("aoc 2018 day 1 part 2:", answer)
