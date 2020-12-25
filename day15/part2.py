numbers = [*map(int, open("input.txt").read().split(','))]

history = dict()
for i, n in enumerate(numbers):
    history[n] = (i+1,)

last = n
for turn in range(len(numbers)+1, 30_000_001):
    last = history[last][-1] - history[last][0]
    if last in history:
        history[last] = (history[last][-1], turn)
    else:
        history[last] = (turn,)
    if turn % 3_000_000 == 0:
        print(turn, last)

print("part2:", last)
