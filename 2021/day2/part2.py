"""advent of code 2021 day 2 part 2"""
inputs = (_.split() for _ in open("input.txt").readlines())

pos = 0
dep = 0
aim = 0
for cmd, val in inputs:
    val = int(val)
    if cmd=="forward":
        pos += val
        dep += aim * val
    if cmd=="down":
        aim += val
    if cmd=="up":
        aim -= val

answer = pos * dep
print("part 2 answer:", answer)
