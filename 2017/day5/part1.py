#!python
"""advent of code 2017 day 5 part 1"""

opcodes = [int(line) for line in open("input.txt").read().splitlines()]

step, ptr = 0, 0
while ptr < len(opcodes):
    # print(ptr, opcodes)
    opcodes[ptr] += 1
    ptr += opcodes[ptr] - 1
    step += 1

print("part 1: {}".format(step))
