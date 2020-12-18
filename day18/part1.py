import re

def parse(sequence):
    seq = sequence.split()
    result = int(seq[0])
    for i, s in enumerate(seq):
        if s=='*':
            result *= int(seq[i+1])
        if s=='+':
            result += int(seq[i+1])
    return str(result)

lines = open("input.txt").read().splitlines()

total = 0
for l in lines:
    while True:
        matches = re.findall("\([^()]+\)", l)
        if not matches:
            break
        for match in matches:
            # print("match:", match)
            result = parse(match.strip('()'))
            l = l.replace(match, result, 1)
    total += int(parse(''.join(l)))

print("part1:", total)
