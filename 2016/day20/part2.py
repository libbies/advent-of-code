blocks = sorted([*map(int, l.split('-'))] for l in open("input.txt").read().splitlines())

queue = blocks.copy()
lengths = list()
while queue:
    block = queue.pop(0)
    for b in queue:
        if b[0] <= block[-1] <= b[-1]:
            queue.remove(b)
            queue.append([min(b[0], block[0]), max(b[-1], block[-1])])
            break
    else:
        queue.append(block)
        if lengths.count(len(queue)) > len(queue):
            break
        lengths.append(len(queue))

count = 2**32
for b in queue:
    count -= b[1] - b[0] + 1

print("part2:", count)
