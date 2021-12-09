"""advent of code 2021 day 6 part 2"""
from collections import Counter

fish = Counter(int(_) for _ in open("input.txt").read().split(','))

for day in range(256):
    fish = {
        k-1: v
        for k, v in fish.items()
    }
    if -1 in fish:
        fish[8] = fish[-1]
        fish[6] = fish[-1] + (fish[6] if 6 in fish else 0)
        del fish[-1]

answer = sum(fish.values())
print("part 2 answer:", answer)
