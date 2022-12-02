#!python
"""advent of code 2022 day 1 part 2"""
answer = sum(sorted(
    sum(int(n) for n in _.split())
    for _ in open("input.txt").read().split("\n\n")
)[-3:])

print("part 2:", answer)
