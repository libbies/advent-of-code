#!python
"""advent of code 2022 day 20 part 1"""
numbers = [int(line) for line in open("input.txt").read().splitlines()]

l = len(numbers)
answers = numbers.copy()
indexes = [*range(l)]
for i, n in enumerate(numbers):
    j = indexes.index(i)
    dst = (j+n)%(l-1)
    _ = indexes.pop(j)
    _ = answers.pop(j)
    indexes.insert(dst, i)
    answers.insert(dst, n)

answer = sum([
    answers[(answers.index(0)+1000)%l],
    answers[(answers.index(0)+2000)%l],
    answers[(answers.index(0)+3000)%l],
])

print("part 1:", answer)
