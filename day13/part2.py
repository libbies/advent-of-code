from functools import reduce
from operator import mul

# modint: https://pypi.org/project/modint/
from modint import chinese_remainder

input = open("input.txt").read().splitlines()

buses = dict()
for offset, bus in enumerate(int(b) if b.isdigit() else None for b in input[1].split(',')):
    if bus:
        buses[bus] = offset

sorted(buses.items(), key=lambda x: x[0])

print("part2:", reduce(mul, buses.keys()) - chinese_remainder(buses.keys(), buses.values()))
