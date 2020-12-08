input = [*map(str.split, open("input.txt").read().splitlines())]

end = len(input) - 1

def run(target, replacement):
    acc, ptr = 0, 0
    history = set()
    while ptr not in history:
        op, value = input[ptr]
        history.add(ptr)
        if ptr == target:
            # print(target, op, replacement)
            op = replacement
        if ptr == end:
            print(f"part2: acc:{acc}; target:{target},{input[target][0]}->{replacement}")
            return(True)
        if op == "acc":
            acc += int(value)
        if op == "nop":
            pass
        if op == "jmp":
            ptr += int(value)
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
