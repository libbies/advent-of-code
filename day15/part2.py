numbers = [*map(int, open("input.txt").read().strip().split(','))]

history = {
    0: list()
}
for i, n in enumerate(numbers):
    history[n] = [i+1]
    # print(i+1, n)

last = n
turn = len(numbers)+1
while turn <= 30000000:
    # print(turn, last, history[last])
    if last in history and len(history[last]) >= 2:
        # spoken twice or more
        last = history[last][-1] - history[last][0]
        if last in history:
            history[last] = [history[last][-1], turn]
        else:
            history[last] = [turn]
    else: # spoken once
        last = 0
        if len(history[0]) >= 2:
            history[0] = [history[0][-1], turn]
        else:
            history[0].append(turn)
    if turn % 3000000 == 0:
        print(turn, last)
    turn += 1

print("part2:", last)
