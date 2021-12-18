#!python
# coding: future_fstrings
"""advent of code 2021 day 18 part 2"""
from itertools import permutations

class Pair(object):
    """a pair"""
    def __init__(self, left, right):
        self.parent = None
        self.left = left if type(left) in (int, Pair) else Pair(*left)
        self.right = right if type(right) in (int, Pair) else Pair(*right)
        if type(self.left)==Pair:
            self.left.parent = self
        if type(self.right)==Pair:
            self.right.parent = self
    def find_to_left(self):
        if not self.parent or self.parent.right==self:
            return self.parent
        return self.parent.find_to_left()
    def find_to_right(self):
        if not self.parent or self.parent.left==self:
            return self.parent
        return self.parent.find_to_right()
    def reduce(self):
        while not self.explode():
            return False
        if self.max>=10:
            while not self.split():
                return False
        return True
    def explode(self):
        for p1 in self: # p0 = self
            if isinstance(p1, int):
                continue
            for p2 in p1:
                if isinstance(p2, int):
                    continue
                for p3 in p2:
                    if isinstance(p3, int):
                        continue
                    for p4 in p3:
                        if isinstance(p4, int):
                            continue
                        if p4.find_to_left():
                            if isinstance(p4.find_to_left().left, int):
                                p4.find_to_left().left += p4.left
                            else: # find the rightmost element of the Pair to the left
                                left = p4.find_to_left().left
                                while isinstance(left, Pair) and isinstance(left.right, Pair):
                                    left = left.right
                                left.right += p4.left
                        if p4.find_to_right():
                            if isinstance(p4.find_to_right().right, int):
                                p4.find_to_right().right += p4.right
                            else: # find the leftmost element of the Pair to the right
                                right = p4.find_to_right().right
                                while isinstance(right, Pair) and isinstance(right.left, Pair):
                                    right = right.left
                                right.left += p4.right
                        if p3.left==p4:
                            p3.left = 0
                        else:
                            p3.right = 0
                        return False
        return True
    def split(self):
        if isinstance(self.left, int) and self.left>=10:
            self.left = Pair(self.left//2, self.left//2 + self.left%2)
            self.left.parent = self
            return False
        if isinstance(self.left, Pair) and not self.left.split():
            return False
        if isinstance(self.right, Pair) and not self.right.split():
            return False
        if isinstance(self.right, int) and self.right>=10:
            self.right = Pair(self.right//2, self.right//2 + self.right%2)
            self.right.parent = self
            return False
        return True
    @property
    def magnitude(self):
        left  = self.left  if isinstance(self.left,  int) else self.left.magnitude
        right = self.right if isinstance(self.right, int) else self.right.magnitude
        return 3*left + 2*right
    def __contains__(self, arg):
        return arg in (self.left, self.right)
    def __iter__(self):
        for _ in (self.left, self.right):
            yield _
    def __repr__(self):
        return f"Pair({self.left},{self.right})"

pairs = [eval(l) for l in open("input.txt").read().splitlines()]
answer = 0
for p in permutations(pairs, 2):
    pair = Pair(*p)
    while not pair.reduce():
        pass
    if pair.magnitude > answer:
        answer = pair.magnitude

print("aoc 2021 day 18 part 2:", answer)
