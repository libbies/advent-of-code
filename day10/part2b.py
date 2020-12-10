inputs = sorted(map(int, open("input.txt").read().splitlines()))

diffs = str()
for i, d in enumerate(inputs):
    diffs += ''.join(str(max(1, d-inputs[i-1])))

print("part1:", diffs.count('1') * (diffs.count('3')+1))

diffs = [d for d in diffs.split('3') if d]

total = 1
for d in diffs:
    if len(d) < 4:
        total *= max(1, 2**(len(d)-1))
    else:
        total *= 2**(len(d)-1)-1

print("part2:", total)
