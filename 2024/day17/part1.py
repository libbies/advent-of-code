#!/usr/bin/env python3
"""advent of code 2024 day 17 part 1"""

lines = open("input.txt").read().splitlines()

A, B, C = 4, 5, 6

registers = dict()
registers[A] = int(lines[0].split()[-1])
registers[B] = int(lines[1].split()[-1])
registers[C] = int(lines[2].split()[-1])

program = [int(_) for _ in lines[-1].split()[-1].split(',')]

ptr = 0
out = list()
while ptr<len(program):
    opcode = program[ptr]
    ptr += 1
    operand = program[ptr]
    if operand==7:
        raise StopIteration
    elif operand in (4,5,6):
        combo = registers[operand]
    else:
        combo = operand
    if opcode==0: # ADV
        registers[A] = registers[A] // 2**combo
    if opcode==1: # BXL
        registers[B] = registers[B] ^ operand
    if opcode==2: # BST
        registers[B] = combo % 8
    if opcode==3: # JNZ
        if registers[A]==0:
            ptr += 1
        else:
            ptr = operand
        continue
    if opcode==4: # BXC
        registers[B] = registers[B] ^ registers[C]
    if opcode==5: # OUT
        out.append(combo % 8)
    if opcode==6: # BDV
        registers[B] = registers[A] // 2**combo
    if opcode==7: # CDV
        registers[C] = registers[A] // 2**combo
    ptr+=1

answer = ','.join(str(_) for _ in out)
print("aoc 2024 day 1 part 1:", answer)
