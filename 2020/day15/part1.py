numbers = [*map(int, open("input.txt").read().strip().split(','))]

history = {
    0: list()
}
for i, n in enumerate(numbers):
    history[n] = [i+1]
    # print(i+1, n)

last = n
turn = len(numbers)+1
while turn <= 2020:
    if last in history and len(history[last]) >= 2:
        # spoken twice or more
        h = history[last][-2:][::-1]
        last = h[0] - h[1]
        if last in history:
            history[last].append(turn)
        else:
            history[last] = [turn]
    else: # spoken once
        last = 0
        history[0].append(turn)
    # print(turn, last)
    turn += 1

print([k for k,v in history.items() if 2020 in v])
