instructions = [l.split(maxsplit=1) for l in open("input.txt").read().splitlines()]


def transmit(n):
    registers = {c: 0 for c in ['a', 'b', 'c', 'd']}
    registers['a'] = n
    len_instructions = len(instructions)
    ptr = 0
    outputs = list()
    while len(outputs) < 100:
        op, val = instructions[ptr]
        if op == "out":
            if val[-1].isdigit():
                output = int(val)
            else:
                output = registers[val]
            if not outputs or ((output == 0 and outputs[-1] == 1)
                            or (output == 1 and outputs[-1] == 0)):
                outputs.append(output)
            else:
                break
        elif op == "tgl":
            if val[-1].isdigit():
                offset = int(val)
            else:
                offset = registers[val]
            if ptr+offset >= len_instructions:
                pass
            else:
                target_op, target_val = instructions[ptr+offset]
                if ' ' in target_val:
                    if target_op == "jnz":
                        instructions[ptr+offset] = ["cpy", target_val]
                    else:
                        instructions[ptr+offset] = ["jnz", target_val]
                else:
                    if target_op == "inc":
                        instructions[ptr+offset] = ["dec", target_val]
                    else:
                        instructions[ptr+offset] = ["inc", target_val]
        elif op == "inc":
            registers[val] += 1
        elif op == "dec":
            registers[val] -= 1
        elif op == "cpy":
            n, target = val.split()
            if target[-1].isdigit():
                pass
            elif n[-1].isdigit():
                registers[target] = int(n)
            else:
                registers[target] = registers[n]
        elif op == "jnz":
            n, offset = val.split()
            if n[-1].isdigit():
                n = int(n)
            else:
                n = registers[n]
            if n != 0:
                if offset[-1].isdigit():
                    offset = int(offset)
                else:
                    offset = registers[offset]
                ptr += int(offset)
                continue
        ptr += 1
    return outputs

for n in range(10000):
    if len(transmit(n)) >= 100:
        print("part1:", n)
        break
