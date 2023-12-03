#!/usr/bin/env python
"""advent of code 2018 day 11 part 1"""
serial = int(open("input.txt").read().strip())

class Cell:
    def __init__(self, x, y, _serial=serial):
        self.x = x
        self.y = y
        self.serial = _serial or serial
    @property
    def rack_id(self):
        return self.x + 10
    @property
    def power(self):
        power = self.rack_id * self.y
        power += self.serial
        power *= self.rack_id
        try:
            power = int(str(power)[-3])
        except IndexError:
            power = 0
        power -= 5
        return power
    def __repr__(self):
        return f"Cell(x={self.x}, y={self.y}, power={self.power})"

grid = {}
for x in range(300):
    for y in range(300):
        grid[x,y] = Cell(x,y)

assert Cell(3, 5, _serial=8).power == 4
assert Cell(122, 79, _serial=57).power == -5
assert Cell(217, 196, _serial=39).power == 0
assert Cell(101, 153, _serial=71).power == 4

best = 0
for x in range(300):
    for y in range(300):
        power = 0
        for i in range(3):
            for j in range(3):
                power += grid[x+i,y+j].power if (x+i,y+j) in grid else 0
        if power > best:
            best = power
            answer = f"{x},{y}"

print("aoc 2018 day 11 part 1:", answer)
