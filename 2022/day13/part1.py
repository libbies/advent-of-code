#!python
"""advent of code 2022 day 13 part 1"""
pairs = [[*map(eval, line.split())] for line in open("input.txt").read().split("\n\n")]

def compare(left, right):
    if type(left)==int and type(right)==int:
        if left < right:
            return True
        elif left > right:
            return False
        else:
            return None
    elif type(left)==int and type(right)==list:
        return compare([left], right)
    elif type(left)==list and type(right)==int:
        return compare(left, [right])
    elif type(left)==list and type(right)==list:
        for i in range(min(len(left), len(right))):
            if compare(left[i], right[i]) is not None:
                return compare(left[i], right[i])
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False
        else:
            return None

answer = 0
for i, (left, right) in enumerate(pairs):
    if compare(left, right):
        answer += i + 1

print("part 1:", answer)
