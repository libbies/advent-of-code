#!/usr/bin/env python3
import sys
from itertools import permutations

POSITION = "0"
IMMEDIATE = "1"
RELATIVE = "2"
LOG = list()

def get_input(inputs):
    return inputs.pop(0)

def get_memory(memory, position):
    try:
        return memory[position]
    except:
        return "oob"

def print_log(log=LOG):
    n = 0
    for item in log:
        print(f"{n:03}: {item}")
        n += 1

def print_memory(memory):
    print({n: memory[n] for n in range(len(memory))})

def print_opcode(opcode):
    if opcode == "99": return "HLT"
    if opcode == "01": return "ADD"
    if opcode == "02": return "MUL"
    if opcode == "03": return "LOD"
    if opcode == "04": return "STO"
    if opcode == "05": return "JMP"
    if opcode == "06": return "JMZ"
    if opcode == "07": return "CML"
    if opcode == "08": return "CMP"
    if opcode == "09": return "RBS"
    return "xxx"

def logger(pointer, instruction, stack, rel_base, memory, log=LOG):
    mode = dict()
    mode[3], mode[2], mode[1], opcode = instruction[0], instruction[1], instruction[2], instruction[-2:]
    log.append([f"{pointer:02}: {instruction}:{print_opcode(opcode)}"] + [
        stack[n] if mode[n] == IMMEDIATE else f"{stack[n]}+{rel_base}:{get_memory(memory, stack[n] if mode[n]==POSITION else stack[n]+rel_base)}"
        for n in range(1, len(stack))
    ])

def execute(memory, ptr, rbase, inputs, outputs, verbose):
    log = list()
    pointer, rel_base, instruction = ptr, rbase, None
    try:
        while True:
            instruction = f"{memory[pointer]:05}"
            mode3, mode2, mode1, opcode = instruction[0], instruction[1], instruction[2], instruction[-2:]
            if opcode == "99":
                stack = [memory[pointer]]
                logger(pointer, instruction, stack, rel_base, memory)
                if verbose:
                    print_log()
                return (True, outputs[-1], 0)
            elif opcode == "01": # ADD - add
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                memory[stack[3] if mode3==POSITION else stack[3]+rel_base] = (
                    (stack[1] if mode1==IMMEDIATE else (memory[stack[1] if mode1==POSITION else stack[1]+rel_base]))
                  + (stack[2] if mode2==IMMEDIATE else (memory[stack[2] if mode2==POSITION else stack[2]+rel_base]))
                )
                pointer += 4
            elif opcode == "02": # MUL - multiply
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                memory[stack[3] if mode3==POSITION else stack[3]+rel_base] = (
                    (stack[1] if mode1==IMMEDIATE else (memory[stack[1] if mode1==POSITION else stack[1]+rel_base]))
                  * (stack[2] if mode2==IMMEDIATE else (memory[stack[2] if mode2==POSITION else stack[2]+rel_base]))
                )
                pointer += 4
            elif opcode == "03": # LOD - read from input
                stack = memory[pointer:pointer+2]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode1 == IMMEDIATE:
                    raise StopIteration
                memory[stack[1] if mode1==POSITION else stack[1]+rel_base] = get_input(inputs)
                pointer += 2
            elif opcode == "04": # STO - write to output
                stack = memory[pointer:pointer+2]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode1 == IMMEDIATE:
                    outputs.append(stack[1])
                else:
                    outputs.append(memory[stack[1] if mode1==POSITION else stack[1]+rel_base])
                pointer += 2
                # return (False, outputs[-1], pointer+2)
            elif opcode == "05": # JMP - jump-if-true
                stack = memory[pointer:pointer+3]
                logger(pointer, instruction, stack, rel_base, memory)
                if (stack[1] if mode1==IMMEDIATE else (memory[stack[1] if mode1==POSITION else stack[1]+rel_base])):
                    pointer = (stack[2] if mode2==IMMEDIATE else (memory[stack[2] if mode2==POSITION else stack[2]+rel_base]))
                else:
                    pointer += 3
            elif opcode == "06": # JMZ - jump-if-false
                stack = memory[pointer:pointer+3]
                logger(pointer, instruction, stack, rel_base, memory)
                if not (stack[1] if mode1==IMMEDIATE else (memory[stack[1] if mode1==POSITION else stack[1]+rel_base])):
                    pointer = (stack[2] if mode2==IMMEDIATE else (memory[stack[2] if mode2==POSITION else stack[2]+rel_base]))
                else:
                    pointer += 3
            elif opcode == "07": # CML - less-than
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                if ((stack[1] if mode1==IMMEDIATE else (memory[stack[1] if mode1==POSITION else stack[1]+rel_base]))
                  < (stack[2] if mode2==IMMEDIATE else (memory[stack[2] if mode2==POSITION else stack[2]+rel_base]))):
                    memory[stack[3] if mode3==POSITION else stack[3]+rel_base] = 1
                else:
                    memory[stack[3] if mode3==POSITION else stack[3]+rel_base] = 0
                pointer += 4
            elif opcode == "08": # CMP - equals
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                if ((stack[1] if mode1==IMMEDIATE else (memory[stack[1] if mode1==POSITION else stack[1]+rel_base]))
                 == (stack[2] if mode2==IMMEDIATE else (memory[stack[2] if mode2==POSITION else stack[2]+rel_base]))):
                    memory[stack[3] if mode3==POSITION else stack[3]+rel_base] = 1
                else:
                    memory[stack[3] if mode3==POSITION else stack[3]+rel_base] = 0
                pointer += 4
            elif opcode == "09": # RBS - rebase
                stack = memory[pointer:pointer+2]
                logger(pointer, instruction, stack, rel_base, memory)
                if mode1 == IMMEDIATE:
                    rel_base += stack[1]
                else:
                    rel_base += memory[stack[1] if mode1==POSITION else stack[1]+rel_base]
                pointer += 2
            else:
                print(f"opcode: {opcode}, {memory}")
                raise StopIteration
    except:
        if verbose:
            # print_log()
            print("...crashed...")
        raise

def main(argv=sys.argv):
    verbose = False
    if "-v" in argv:
        verbose = True

    f = argv[-1]

    code = [int(n) for n in open(f, 'r').read().strip().split(',')]
    print(f"executing {len(code)-1} opcodes")

    results = list()
    halted = False

    signal, iteration, rbase, halted = 0, 0, 0, False
    inputs = [ 2 ]
    outputs = list()
    pointer = 0
    memory = list(code) + [0]*1024*1024
    (halted, signal, ptr) = execute(memory, pointer, rbase, inputs, outputs, verbose)
    print(outputs)
    if verbose:
        print(f"results: {results}")

if __name__ == "__main__":
    main()
