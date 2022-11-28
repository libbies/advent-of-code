#!python
"""advent of code 2017 day 6 part 1"""

mem = [int(_) for line in open("input.txt").read().splitlines() for _ in line.split()]

step = 0
prev = list()
l = len(mem)
step = 0
while True:
    block = max(mem)
    idx = mem.index(block)
    print(mem)
    mem[idx] = 0
    mem = list(map(lambda x: x + (block//l), mem))
    print(mem)
    step += 1



print("part 1: {}".format(step))
