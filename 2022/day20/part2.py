#!python
"""advent of code 2022 day 20 part 2"""
numbers = [int(line) * 811589153 for line in open("input.txt").read().splitlines()]

l = len(numbers)
answers = numbers.copy()
indexes = [*range(l)]
for _ in range(10): # lolwat
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

print("part 2:", answer)
