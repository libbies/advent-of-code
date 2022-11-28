#!/usr/bin/env python3

code = [int(n) for n in open('input.txt', 'r').read().strip().split(',')]
pointer = 0
eof = len(code) - 1

print(f"executing {eof} opcodes")

memory = code
pointer, instruction, memory = 0, None, list(code)

inputs = [ 1 ]
log = list()

POSITION = "0"
IMMEDIATE = "1"

def get_input():
    return inputs.pop(0)

def get_memory(position):
    try:
        return memory[position]
    except:
        return "oob"

def print_log(log):
    n = 0
    for item in log:
        print(f"{n:02}: {item}")
        n += 1
    print(f"last instruction {instruction}, {memory}")

def logger(instruction, stack):
    mode = dict()
    mode[3], mode[2], mode[1], opcode = instruction[0], instruction[1], instruction[2], instruction[-2:]
    log.append([instruction] + [
        stack[n] if mode[n] == IMMEDIATE else f"{stack[n]}p{get_memory(stack[n])}"
        for n in range(1, len(stack))
    ])

try:
    while True:
        instruction = f"{memory[pointer]:05}"
        mode3, mode2, mode1, opcode = instruction[0], instruction[1], instruction[2], instruction[-2:]
        if opcode == "99":
            print(f"halting execution")
            print_log(log)
            break
        elif opcode == "01": # add
            stack = memory[pointer:pointer+4]
            logger(instruction, stack)
            if mode3 == IMMEDIATE:
                raise StopIteration
            elif mode3 == POSITION:
                memory[stack[3]] = (
                    (stack[1] if mode1 == IMMEDIATE else memory[stack[1]])
                  + (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])
                )
            pointer += 4
        elif opcode == "02": # multiply
            stack = memory[pointer:pointer+4]
            logger(instruction, stack)
            if mode3 == IMMEDIATE:
                raise StopIteration
            elif mode3 == POSITION:
                memory[stack[3]] = (
                    (stack[1] if mode1 == IMMEDIATE else memory[stack[1]])
                  * (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])
                )
            pointer += 4
        elif opcode == "03": # write
            stack = memory[pointer:pointer+2]
            logger(instruction, stack)
            if mode1 == IMMEDIATE:
                raise StopIteration
            elif mode1 == POSITION:
                memory[stack[1]] = get_input()
            pointer += 2
        elif opcode == "04": # read
            stack = memory[pointer:pointer+2]
            logger(instruction, stack)
            if mode1 == IMMEDIATE:
               print(f"output(immediate) {stack[1]}")
            elif mode1 == POSITION:
                print(f"output(position) {memory[stack[1]]}")
            else:
                raise StopIteration
            pointer += 2
        else:
            print(f"opcode: {opcode}, {memory}")
            raise StopIteration
except:
    print_log(log)
    raise
