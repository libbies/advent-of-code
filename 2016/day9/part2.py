from collections import deque

lines = open("input.txt").read().splitlines()

def decompress(input):
    l = len(input)
    input = deque(input)
    # output = str()
    len_output = 0
    buffer = list()
    while input:
        c = input.popleft()
        if buffer and c != ')':
            buffer.append(c)
        elif buffer and c == ')':
            count, repeat = map(int, ''.join(buffer).strip('(').split('x'))
            segment = ''.join(input.popleft() for _ in range(count))
            len_output += decompress(segment) * repeat
            buffer = list()
        elif c != '(':
            len_output += 1
        elif c == '(':
            buffer.append('(')
        else:
            raise ValueError
    return len_output

for line in lines:
    output = decompress(line)
    print("part2:", output)
