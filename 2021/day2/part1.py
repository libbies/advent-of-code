"""advent of code 2021 day 2 part 1"""
inputs = (_.split() for _ in open("input.txt").readlines())

pos = 0
dep = 0
for cmd, val in inputs:
    val = int(val)
    if cmd=="forward":
        dep += val
    if cmd=="down":
        pos += val
    if cmd=="up":
        pos -= val

answer = pos * dep
print("part 1 answer:", answer)
