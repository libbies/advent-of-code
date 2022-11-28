from collections import deque

lines = open("input.txt").read().splitlines()

def decompress(input):
    l = len(input)
    input = deque(input)
    output = str()
    buffer = list()
    while input:
        c = input.popleft()
        if buffer and c != ')':
            buffer.append(c)
        elif buffer and c == ')':
            count, repeat = map(int, ''.join(buffer).strip('(').split('x'))
            output += ''.join(input.popleft() for _ in range(count)) * repeat
            buffer = list()
        elif c != '(':
            output += c
        elif c == '(':
            buffer.append('(')
    return output

for line in lines:
    output = decompress(line)
    print("part1:", len(output))
