import re

def parse(seq):
    while '+' in seq:
        match = re.search("[0-9]+([+][0-9]+)+", seq)
        result = eval(match.group(0))
        # print(match.group(0), '=', result)
        seq = seq.replace(match.group(0), str(result), 1)
        # print(seq)
    result = eval(seq)
    return str(result)

lines = open("input.txt").read().splitlines()

total = 0
for l in lines:
    # print(l)
    l = ''.join(l.split())
    while '(' in l:
        # print("l:", l)
        match = re.search("\([^()]+\)", l)
        result = parse(match.group(0))
        # print("match:", match.group(0), result)
        l = l.replace(match.group(0), result, 1)
    result = int(parse(l))
    # print("result:", result)
    total += result

print("part2:", total)
