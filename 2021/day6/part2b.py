"""advent of code 2021 day 6 part 2"""
from collections import Counter, defaultdict

fish = Counter(int(_) for _ in open("input.txt").read().split(','))
days = 256

for day in range(days%7):
    fish = {
        k-1: v
        for k, v in fish.items()
    }
    if -1 in fish:
        fish[8] = fish[-1]
        fish[6] = fish[-1] + (fish[6] if 6 in fish else 0)
        del fish[-1]

fish = defaultdict(int, fish)

for day in range(days//7):
    fish[8], fish[7], fish[6], fish[5], fish[4], fish[3], fish[2], fish[1], fish[0] = \
        fish[6], \
        fish[5], \
        fish[6] + fish[4], \
        fish[5] + fish[3], \
        fish[4] + fish[2], \
        fish[3] + fish[1], \
        fish[2] + fish[0], \
        fish[1] + fish[8], \
        fish[0] + fish[7]

answer = sum(fish.values())
print("part 2 answer:", answer)
