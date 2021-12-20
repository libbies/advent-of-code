#!python
"""advent of code 2021 day 19 part 1"""
from collections import Counter
from itertools import product, permutations

class Beacon(object):
    __slots__ = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return f"Beacon({self.x},{self.y},{self.z})"
    def __getitem__(self, key):
        return self.__getattribute__(key)

lines = open("input.txt").read().splitlines()
scanners = dict()
for line in lines:
    if line.startswith("---"):
        scanner = int(line.split()[-2])
        scanners[scanner] = []
    elif line:
        scanners[scanner].append(Beacon(*map(int, line.split(","))))

offsets, scanned = [], []
aligned = [0]
while [s for s in scanners if s not in aligned]:
    for s1 in aligned:
        if s1 in scanned:
            continue
        for s2 in scanners:
            for cx, cy, cz in permutations(('x', 'y', 'z')):
                for sx, sy, sz in product((1, -1), (1, -1), (1, -1)):
                    if s2 in aligned:
                        break
                    count = Counter((b1.x-sx*b2[cx], b1.y-sy*b2[cy], b1.z-sz*b2[cz])
                            for b1 in scanners[s1]
                            for b2 in scanners[s2]).most_common()
                    if count[0][-1]>=12:
                        ox, oy, oz = count[0][0]
                        print(f"aligning s{s2} to s{s1}")
                        offsets.append(count[0][0])
                        scanners[s2] = [Beacon(sx*b[cx]+ox, sy*b[cy]+oy, sz*b[cz]+oz) for b in scanners[s2]]
                        aligned.append(s2)
        scanned.append(s1)

answer = max(sum([abs(x1-x2), abs(y1-y2), abs(z1-z2)])
            for x1, y1, z1 in offsets
            for x2, y2, z2 in offsets)
print("aoc 2021 day 19 part 2:", answer)
