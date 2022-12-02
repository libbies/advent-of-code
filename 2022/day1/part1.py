#!python
"""advent of code 2022 day 1 part 1"""
answer = max(
    sum(int(n) for n in _.split())
    for _ in open("input.txt").read().split("\n\n")
)

print("part 1:", answer)
