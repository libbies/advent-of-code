#!python
"""advent of code 2021 day 24 part 1"""
from pprint import pprint
lines = [l.split() for l in open("input.txt").read().splitlines()]

def cleanup(regs):
    for register in regs:
        regs[register] = regs[register].replace("(0*0)", "0").replace("(0+", "(")

i = 0
registers = {"w":"0", "x":"0", "y":"0", "z":"0"}
for line in lines:
    if line[0]=="inp":
        if i>0:
            print(registers)
        if i>3:
            break
        registers["w"] = f"model[{i}]"
        i += 1
    elif line[0]=="add":
        if line[2].lstrip("-").isdigit():
            if line[2]=="0":
                continue
            if registers[line[1]]=="0":
                registers[line[1]] = line[2]
            else:
                registers[line[1]] = f"({registers[line[1]]}+{line[2]})"
        else:
            if registers[line[2]]=="0":
                continue
            if registers[line[1]]=="0":
                registers[line[1]] = registers[line[2]]
            else:
                registers[line[1]] = f"({registers[line[1]]}+{registers[line[2]]})"
    elif line[0]=="mul":
        if registers[line[1]]=="0" or line[2]=="0":
            registers[line[1]] = "0"
        elif line[2]=="1":
            continue
        elif line[2].lstrip("-").isdigit():
            if registers[line[1]]=="1":
                registers[line[1]] = line[2]
            else:
                registers[line[1]] = f"({registers[line[1]]}*{line[2]})"
        else:
            if registers[line[1]]=="1":
                registers[line[1]] = registers[line[2]]
            elif registers[line[2]]=="1":
                continue
            else:
                registers[line[1]] = f"({registers[line[1]]}*{registers[line[2]]})"
    elif line[0]=="div":
        if registers[line[1]]=="0" or line[2]=="1":
            continue
        elif line[2].lstrip("-").isdigit():
            registers[line[1]] = f"({registers[line[1]]}//{line[2]})"
        else:
            registers[line[1]] = f"({registers[line[1]]}//{registers[line[2]]})"
    elif line[0]=="mod":
        if line[2].lstrip("-").isdigit():
            registers[line[1]] = f"({registers[line[1]]}%{line[2]})"
        else:
            registers[line[1]] = f"({registers[line[1]]}%{registers[line[2]]})"
    elif line[0]=="eql":
        if line[2].lstrip("-").isdigit():
            if line[2]==registers[line[1]]:
                registers[line[1]] = "1"
            else:
                registers[line[1]] = f"({registers[line[1]]}=={line[2]})"
        elif line[2]=="w" and registers[line[1]].lstrip('-').isdigit() and int(registers[line[1]])>9:
            registers[line[1]] = "0"
        elif registers[line[1]]==registers[line[2]]:
            registers[line[1]] = "1"
        else:
            registers[line[1]] = f"({registers[line[1]]}=={registers[line[2]]})"
print([len(r) for r in registers.values()])
print([r[:300] for r in registers.values()])

answer = 0
print("aoc 2021 day 24 part 1:", answer)
