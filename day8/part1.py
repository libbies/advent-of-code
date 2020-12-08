input = map(str.split, open("input.txt").read().splitlines())

acc = 0
ptr = 0
history = set()
while ptr not in history:
    op, value = input[ptr]
    history.add(ptr)
    if op == "acc":
        acc += int(value)
    if op == "nop":
        pass
    if op == "jmp":
        ptr = ptr + int(value)
    else:
        ptr += 1

print("part1:", acc)
