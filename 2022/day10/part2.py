#!python
"""advent of code 2022 day 10 part 2"""
from pprint import pprint
lines = [line.split() for line in open("input.txt").read().splitlines()]

cycle = 1
registers = { 'X': 1 }
display = [[' '] * 40 for _ in range(6)]
for line in lines:
    if line[0] == "noop":
        if registers['X'] <= cycle%40 <= registers['X']+2:
            display[cycle//40][cycle%40] = '█'
        cycle += 1
    elif line[0] == "addx":
        if registers['X'] <= cycle%40 <= registers['X']+2:
            display[cycle//40][cycle%40] = '█'
        cycle += 1
        if registers['X'] <= cycle%40 <= registers['X']+2:
            display[cycle//40][cycle%40] = '█'
        cycle += 1
        registers['X'] += int(line[-1])

print("part 2:")
print('\n'.join(''.join(_[1:]) for _ in display))
