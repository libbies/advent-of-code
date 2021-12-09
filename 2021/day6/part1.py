"""advent of code 2021 day 6 part 1"""
fish = [int(_) for _ in open("input.txt").read().split(',')]

for day in range(80):
    fish = [f-1 if f!=0 else 6 for f in fish] + [8] * fish.count(0)

answer = len(fish)
print("part 1 answer:", answer)
