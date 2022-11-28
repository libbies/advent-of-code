instructions = [l.split(maxsplit=1) for l in open("input.txt").read().splitlines()]

registers = {c: 0 for c in ['a', 'b', 'c', 'd']}

ptr = 0
while ptr != len(instructions):
    op, val = instructions[ptr]
    if op == "inc":
        registers[val] += 1
    elif op == "dec":
        registers[val] -= 1
    elif op == "cpy":
        n, target = val.split()
        if n.isdigit():
            registers[target] = int(n)
        else:
            registers[target] = registers[n]
    elif op == "jnz":
        n, offset = val.split()
        if n.isdigit():
            n = int(n)
        else:
            n = registers[n]
        if n != 0:
            ptr += int(offset)
            continue
    ptr += 1

print(registers, "part1:", registers['a'])
