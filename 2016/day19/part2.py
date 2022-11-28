from collections import deque

elves = list(range(1, 1+int(open("input.txt").read().strip())))
winners, losers = deque(elves[:len(elves)//2]), deque(elves[len(elves)//2:])

while winners and losers:
    target = losers.popleft()
    losers.append(winners.popleft())
    winners.append(losers.popleft())
    if len(winners) > len(losers):
        losers.appendleft(winners.pop())

print("part2:", winners or losers)
