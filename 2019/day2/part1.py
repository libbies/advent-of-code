#!/usr/bin/env python3

code = [int(n) for n in open('input.txt', 'r').read().strip().split(',')]
pointer = 0
eof = len(code) - 1

code[1] = 12
code[2] = 2 
print(f"executing {eof} opcodes")

while True:
    stack = code[pointer:min(eof, pointer+4)]
    print(stack)
    if not stack or stack[0]==99:
        break
    elif stack[0]==1:
        if [n for n in stack[1:] if n > eof]:
            break
        code[stack[3]] = code[stack[2]] + code[stack[1]]
    elif stack[0]==2:
        if [n for n in stack[1:] if n > eof]:
            raise(StopIteration)
        code[stack[3]] = code[stack[2]] * code[stack[1]]
    else:
        break
    pointer += 4

print(code)
