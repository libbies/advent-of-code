#!python
"""advent of code 2021 day 24 part 1"""
lines = [l.split(maxsplit=1) for l in open("input.txt").read().splitlines()]

memo = dict()
for n in range(99999999999999, 11111111111111, -1):
    registers = {"w": 0, "x": 0, "y": 0, "z": 0}
    discard = []
    s = [int(c) for c in str(n)]
    if 0 in s:
        continue
    for op, val in lines:
        if op == "inp":
            print(registers)
            registers[val] = s.pop(0)
            continue
        v1, v2 = val.split()
        if op == "add":
            if v2.lstrip("-").isdigit():
                registers[v1] += int(v2)
            else:
                registers[v1] += registers[v2]
        elif op == "mul":
            if v2.lstrip("-").isdigit():
                if int(v2) == 0:
                    registers[v1] = 0
                else:
                    registers[v1] *= int(v2)
            else:
                registers[v1] *= registers[v2]
        elif op == "div":
            if v2.lstrip("-").isdigit():
                assert v2 != "0"
                registers[v1] //= int(v2)
            else:
                registers[v1] //= registers[v2]
        elif op == "mod":
            if v2.lstrip("-").isdigit():
                assert registers[v1] >= 0 and int(v2) > 0
                registers[v1] %= int(v2)
            else:
                assert registers[v1] >= 0 and registers[v2] > 0
                registers[v1] %= registers[v2]
        elif op == "eql":
            if v2.lstrip("-").isdigit():
                if registers[v1] == int(v2):
                    registers[v1] = 1
                else:
                    registers[v1] = 0
            elif registers[v1] == registers[v2]:
                registers[v1] = 1
            else:
                registers[v1] = 0
    if registers["z"] == 0:
        answer = n
        break
    elif n % 10000 == 9999:
        print(n)

answer = 0
print("aoc 2021 day 24 part 1:", answer)
