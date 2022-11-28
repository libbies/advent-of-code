from collections import deque

instructions = [l.split(maxsplit=1) for l in open("input.txt").read().splitlines()]

password = list("abcdefgh")
for op, val in instructions:
    # print(''.join(password), "=>", op, val)
    if op == "swap":
        type, x, _, _, y = val.split()
        if type == "position":
            password[int(x)], password[int(y)] = password[int(y)], password[int(x)]
        elif type == "letter":
            px, py = password.index(x),password.index(y)
            password[px], password[py] = y, x
    elif op == "reverse":
        _, x, _, y = val.split()
        x, y = int(x), int(y)
        password = password[:x] + password[x:y+1][::-1] + password[y+1:]
    elif op == "rotate":
        val = val.split()
        if val[0] == "left":
            offset = int(val[1])
            password = deque(password)
            password.rotate(-offset)
            password = list(password)
        elif val[0] == "right":
            offset = int(val[1])
            password = deque(password)
            password.rotate(offset)
            password = list(password)
        elif val[0] == "based":
            offset = password.index(val[-1])
            if offset >= 4:
                offset += 1
            password = deque(password)
            password.rotate(offset+1)
            password = list(password)
    elif op == "move":
        _, x, _, _, y = val.split()
        password.insert(int(y), password.pop(int(x)))
    else:
        raise RuntimeError

print("part1:", ''.join(password))
