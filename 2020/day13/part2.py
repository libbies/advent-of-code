from functools import reduce
from operator import mul

def crt(n, a):
    p = reduce(mul, n)
    return sum(ai * pow(p//ni, -1, ni) * (p//ni) for (ni, ai) in zip(n, a)) % p

input = [
    int(b) if b.isdigit() else None
    for b in open("input.txt").read().splitlines()[-1].split(',')
]

buses = dict()
for offset, bus in enumerate(input):
    if bus:
        buses[bus] = offset

print("part2:", reduce(mul, buses.keys()) - crt(buses.keys(), buses.values()))
