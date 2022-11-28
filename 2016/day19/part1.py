from collections import deque
elves = deque(range(1, 1+int(open("input.txt").read().strip())))

ptr = 0
while len(elves) > 1:
    elves.rotate(-1)
    elves.popleft()

print("part1:", elves)
