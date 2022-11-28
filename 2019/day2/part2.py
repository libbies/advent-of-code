#!/usr/bin/env python3

code = [int(n) for n in open('input.txt', 'r').read().strip().split(',')]
pointer = 0
eof = len(code) - 1

print(f"executing {eof} opcodes")

memory = code
for noun in range(100):
    for verb in range(100):
        pointer, memory = 0, list(code)
        memory[1], memory[2] = noun, verb
        # print(f"{noun} {verb} {memory}")
        while True:
            stack = memory[pointer:min(eof, pointer+4)]
            # print(stack)
            if not stack or stack[0]==99:
                break
            elif stack[0]==1:
                if [n for n in stack[1:] if n > eof]:
                    break
                memory[stack[3]] = memory[stack[2]] + memory[stack[1]]
            elif stack[0]==2:
                if [n for n in stack[1:] if n > eof]:
                    break
                memory[stack[3]] = memory[stack[2]] * memory[stack[1]]
            else:
                break
            pointer += 4
        # print(f"{noun} {verb} {memory}")
        if memory[0] == 19690720:
            print(f"100 * {noun} + {verb} = {100 * noun + verb}")
            raise(StopIteration)
