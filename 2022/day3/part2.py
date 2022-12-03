#!python
"""advent of code 2022 day 3 part 2"""
sacks = [set(_) for _ in open("input.txt").read().splitlines()]

groups = zip(*(iter(sacks),) * 3)

sum = 0
for (s1, s2, s3) in groups:
    item = [item for item in s1 if item in s2 if item in s3].pop()
    if item.islower():
        sum += ord(item) - 96
    if item.isupper():
        sum += ord(item) - 64 + 26

print("part 2:", sum)
