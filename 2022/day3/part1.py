#!python
"""advent of code 2022 day 3 part 1"""
sacks = [
    (set(l[:len(l)//2]), set(l[len(l)//2:]))
    for l in open("input.txt").read().splitlines()
]

dupes = [
    [item for item in sack[0] if item in sack[-1]].pop()
    for sack in sacks
]

sum = 0
for item in dupes:
    if item.islower():
        sum += ord(item) - 96
    if item.isupper():
        sum += ord(item) - 64 + 26

print("part 1:", sum)
