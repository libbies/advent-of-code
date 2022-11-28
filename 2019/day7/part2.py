#!/usr/bin/env python3
import sys
from itertools import permutations

POSITION = "0"
IMMEDIATE = "1"
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
    return "xxx"

def logger(pointer, instruction, stack, memory, log=LOG):
    mode = dict()
    mode[3], mode[2], mode[1], opcode = instruction[0], instruction[1], instruction[2], instruction[-2:]
    log.append([f"{pointer:02}: {instruction}:{print_opcode(opcode)}"] + [
        stack[n] if mode[n] == IMMEDIATE else f"{stack[n]}:{get_memory(memory, stack[n])}"
        for n in range(1, len(stack))
    ])

def execute(memory, ptr, inputs, outputs, verbose):
    log = list()
    pointer, instruction = ptr, None
    try:
        while True:
            instruction = f"{memory[pointer]:05}"
            mode3, mode2, mode1, opcode = instruction[0], instruction[1], instruction[2], instruction[-2:]
            if opcode == "99":
                stack = [memory[pointer]]
                logger(pointer, instruction, stack, memory)
                #if verbose:
                #    print_log()
                return (True, outputs[-1], 0)
            elif opcode == "01": # ADD - add
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                elif mode3 == POSITION:
                    memory[stack[3]] = (
                        (stack[1] if mode1 == IMMEDIATE else memory[stack[1]])
                      + (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])
                    )
                pointer += 4
            elif opcode == "02": # MUL - multiply
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                elif mode3 == POSITION:
                    memory[stack[3]] = (
                        (stack[1] if mode1 == IMMEDIATE else memory[stack[1]])
                      * (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])
                    )
                pointer += 4
            elif opcode == "03": # LOD - read from input
                stack = memory[pointer:pointer+2]
                logger(pointer, instruction, stack, memory)
                if mode1 == IMMEDIATE:
                    raise StopIteration
                elif mode1 == POSITION:
                    memory[stack[1]] = get_input(inputs)
                pointer += 2
            elif opcode == "04": # STO - write to output
                stack = memory[pointer:pointer+2]
                logger(pointer, instruction, stack, memory)
                if mode1 == IMMEDIATE:
                    # print(f"output(immediate) {stack[1]}")
                    outputs.append(stack[1])
                elif mode1 == POSITION:
                    # print(f"output(position:{stack[1]}) {memory[stack[1]]}")
                    outputs.append(memory[stack[1]])
                return (False, outputs[-1], pointer+2)
            elif opcode == "05": # JMP - jump-if-true
                stack = memory[pointer:pointer+3]
                logger(pointer, instruction, stack, memory)
                if (stack[1] if mode1 == IMMEDIATE else memory[stack[1]]):
                    pointer = (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])
                else:
                    pointer += 3
            elif opcode == "06": # JMZ - jump-if-false
                stack = memory[pointer:pointer+3]
                logger(pointer, instruction, stack, memory)
                if not (stack[1] if mode1 == IMMEDIATE else memory[stack[1]]):
                    pointer = (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])
                else:
                    pointer += 3
            elif opcode == "07": # CML - less-than
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                elif mode3 == POSITION:
                    if ((stack[1] if mode1 == IMMEDIATE else memory[stack[1]])
                      < (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])):
                        memory[stack[3]] = 1
                    else:
                        memory[stack[3]] = 0
                    pointer += 4
            elif opcode == "08": # CMP - equals
                stack = memory[pointer:pointer+4]
                logger(pointer, instruction, stack, memory)
                if mode3 == IMMEDIATE:
                    raise StopIteration
                elif mode3 == POSITION:
                    if ((stack[1] if mode1 == IMMEDIATE else memory[stack[1]])
                     == (stack[2] if mode2 == IMMEDIATE else memory[stack[2]])):
                        memory[stack[3]] = 1
                    else:
                        memory[stack[3]] = 0
                    pointer += 4
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

    for phases in permutations(range(5, 10)):
        signal, iteration, halted = 0, 0, False
        inputs, outputs, pointer, memory = dict(), dict(), dict(), dict()
        for phase in phases:
            inputs[phase] = [phase]
            outputs[phase] = list()
            pointer[phase] = 0
            memory[phase] = list(code)
        while not halted:
            for phase in phases:
                inputs[phase] += [signal]
                (halted, signal, ptr) = execute(memory[phase], pointer[phase], inputs[phase], outputs[phase], verbose)
                if halted and phase == phases[-1]:
                    if verbose:
                        print(f"hlt:{halted} i:{iteration} p:{phase} inputs:{inputs[phase]} ptr:{pointer[phase]} signal:{signal}")
                    break
                pointer[phase] = ptr
            iteration += 1
        results += [signal]
    if verbose:
        print(f"results: {results}")
    print(f"computed {len(results)} signals, max: {max(results)}")

if __name__ == "__main__":
    main()
