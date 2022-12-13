#!python
"""advent of code 2022 day 13 part 1"""
pairs = [[*map(eval, line.split())] for line in open("input.txt").read().split("\n\n")]

def compare(left, right):
    if type(left)==int and type(right)==int:
        return (left < right) if left!=right else None
    elif type(left)==int and type(right)==list:
        return compare([left], right)
    elif type(left)==list and type(right)==int:
        return compare(left, [right])
    elif type(left)==list and type(right)==list:
        for i in range(min(len(left), len(right))):
            if compare(left[i], right[i]) is not None:
                return compare(left[i], right[i])
        return len(left) < len(right) if len(left)!=len(right) else None

answer = sum(i+1 for i, (left, right) in enumerate(pairs) if compare(left, right))

print("part 1:", answer)
