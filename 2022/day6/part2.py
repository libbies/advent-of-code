#!python
"""advent of code 2022 day 6 part 2"""
from collections import Counter
data = open("input.txt").read().strip()

for i in range(len((data))):
    segment = data[i:i+14]
    if max(Counter(segment).values()) == 1:
        answer = i + 14
        break

print("part 2:", answer)
