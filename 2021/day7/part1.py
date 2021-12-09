"""advent of code 2021 day 7 part 1"""
positions = [int(_) for _ in open("input.txt").read().split(',')]

# median = sorted(positions)[len(positions)//2]

answer = min(
    sum(abs(p-n) for p in positions)
    for n in range(max(positions))
)

print("part 1 answer:", answer)
