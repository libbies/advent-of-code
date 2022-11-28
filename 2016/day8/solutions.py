import numpy
from pprint import pprint

instructions = [l.split(maxsplit=1) for l in open("input.txt").read().splitlines()]

row = [' '] * 50
grid = numpy.array([row.copy(), row.copy(), row.copy(),
                    row.copy(), row.copy(), row.copy()])

for op, val in instructions:
    if op == "rect":
        y, x = map(int, val.split('x'))
        grid[:x,:y] = '#'
    if op =="rotate":
        _, target, _, shift = val.split()
        t, tid = target.split('=')
        tid, shift = int(tid), int(shift)
        if target[0] == 'x':
            grid[:,tid] = numpy.roll(grid[:,tid], shift)
        elif target[0] == 'y':
            grid[tid,:] = numpy.roll(grid[tid,:], shift)

print("part1:", numpy.count_nonzero(grid=='#'))
print("part2:")
pprint([''.join(r) for r in grid])
