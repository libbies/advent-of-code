#!python
"""advent of code 2022 day 4 part 1"""
numbers = [_.split(',') for _ in open("input.txt").read().splitlines()]

count = 0
for p1, p2 in numbers:
    a1, a2 = map(int, p1.split('-'))
    b1, b2 = map(int, p2.split('-'))
    if a1 <= b1 and b2 <= a2:
        count += 1
    elif b1 <= a1 and a2 <= b2:
        count += 1

print("part 1:", count)
