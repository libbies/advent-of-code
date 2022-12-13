#!python
"""advent of code 2022 day 13 part 2"""
from functools import cmp_to_key
pairs = [[*map(eval, line.split())] for line in open("input.txt").read().split()]
pairs.extend([[], [[2]], [[6]]])

def compare(left, right):
    if type(left)==int and type(right)==int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif type(left)==int and type(right)==list:
        return compare([left], right)
    elif type(left)==list and type(right)==int:
        return compare(left, [right])
    elif type(left)==list and type(right)==list:
        for i in range(min(len(left), len(right))):
            if compare(left[i], right[i]):
                return compare(left[i], right[i])
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0

pairs.sort(key=cmp_to_key(compare))
answer = pairs.index([[2]]) * pairs.index([[6]])

print("part 2:", answer)
