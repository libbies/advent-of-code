from functools import reduce
from operator import mul

input = open("input.txt").read().splitlines()

buses = dict()
for offset, bus in enumerate(int(b) if b.isdigit() else None for b in input[1].split(',')):
    if bus:
        buses[bus] = offset

def crt(n, a):
    p = reduce(mul, n)
    return sum(ai * pow(p//ni, -1, ni) * (p//ni) for (ni, ai) in zip(n, a)) % p

print("part2:", reduce(mul, buses.keys()) - crt(buses.keys(), buses.values()))
