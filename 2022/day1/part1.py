#!python
"""advent of code 2022 day 1 part 1"""
answer = max(
    sum(int(calorie) for calorie in elf.split())
    for elf in open("input.txt").read().split("\n\n")
)

print("part 1:", answer)
