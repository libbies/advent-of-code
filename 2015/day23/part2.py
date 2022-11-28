input = [
    (k, v.split(', '))
    for k, v in (
        l.split(maxsplit=1) for l in open("input.txt").read().splitlines()
    )
]

registers = {
    "a": 1,
    "b": 0,
}

l = len(input)
ptr = 0
while ptr != l:
    op, values = input[ptr]
    if op == "hlf": # half
        registers[values[0]] //= 2
    elif op == "tpl": # triple
        registers[values[0]] *= 3
    elif op == "inc": # increment
        registers[values[0]] += 1
    if op == "jmp": # jump
        ptr += int(values[0])
    elif op == "jie" and registers[values[0]] % 2 == 0:
            ptr += int(values[-1])
    elif op == "jio" and registers[values[0]] == 1:
            ptr += int(values[-1])
    else:
        ptr += 1
    # print(op, values, registers)

print(registers, "part1:", registers["b"])
