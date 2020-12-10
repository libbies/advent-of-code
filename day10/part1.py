input = sorted(map(int, open("input.txt").read().splitlines()))

diff = list()
for c in range(1, len(input)):
    diff.append(input[c] - input[c-1])

print(diff.count(3)+1, diff.count(1)+1, 'part1:',
    (diff.count(3)+1) * (diff.count(1)+1))
