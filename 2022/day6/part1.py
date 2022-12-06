#!python
"""advent of code 2022 day 6 part 1"""
from collections import Counter
data = open("input.txt").read().strip()

for i in range(len((data))):
    segment = data[i:i+4]
    if max(Counter(segment).values()) == 1:
        answer = i + 4
        break

print("part 1:", answer)
