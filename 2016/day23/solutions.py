from functools import reduce
from operator import mul
instructions = [l.split(maxsplit=1) for l in open("input.txt").read().splitlines()]

registers = {c: 0 for c in ['a', 'b', 'c', 'd']}
registers['a'] = 7

len_instructions = len(instructions)
prev = 0
ptr = 0
while ptr != len_instructions:
    op, val = instructions[ptr]
    if op == "tgl":
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
    if registers['b'] != prev:
        prev = registers['b']
        print(registers)
        # {'a': 7, 'b': 7, 'c': 0, 'd': 0}
        # {'a': 7, 'b': 6, 'c': 0, 'd': 0}
        # {'a': 42, 'b': 5, 'c': 0, 'd': 0}    # a = 7*6
        # {'a': 210, 'b': 4, 'c': 0, 'd': 0}   # a = 7*6*5
        # {'a': 840, 'b': 3, 'c': 0, 'd': 0}   # a = 7*6*5*4
        # {'a': 2520, 'b': 2, 'c': 0, 'd': 0}  # a = 7*6*5*4*3
        # {'a': 5040, 'b': 1, 'c': 0, 'd': 0}  # a = 7*6*5*4*3*2
        # {'a': 13776, 'b': 1, 'c': 0, 'd': 0} # a = 7*6*5*4*3*2 + n?
        #
        # 5040 = 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
        # 13776 - 5040 = 8736 = 96 * 91
        #
        # cpy 96 c
        # jnz 91 d

print(registers, '\n' + "part1:", registers['a'])

n = registers['a'] - reduce(mul, range(1, 7+1))
print("n:", n, '+', reduce(mul, range(1, 12+1)), "part2:", reduce(mul, range(1, 12+1)) + n)
