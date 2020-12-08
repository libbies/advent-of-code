input = [*map(str.split, open("input.txt").read().splitlines())]

end = len(input) - 1

def run(target, replacement):
    acc = 0
    ptr = 0
    history = set()
    attempts = 0
    while ptr not in history:
        op, value = input[ptr]
        if ptr == target:
            # print(ptr, target, op, replacement)
            op = replacement
        history.add(ptr)
        if ptr == end:
            print(f"part2: target:{target}, acc:{acc}")
            return(True)
        if op == "acc":
            acc += int(value)
        if op == "nop":
            pass
        if op == "jmp":
            ptr = ptr + int(value)
        else:
            ptr += 1
    return(False)

for i, (op, acc) in enumerate(input):
    if op=="nop":
        if run(i, "jmp"):
            break
    elif op=="jmp":
        if run(i, "nop"):
            break
