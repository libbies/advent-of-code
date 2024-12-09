#!/usr/bin/env python3
"""advent of code 2024 day 9 part 2"""

diskmap = open("input.txt").read().strip()
blocks = iter(diskmap[i:i+2] for i in range(0, len(diskmap), 2))

cursor = 0
file_id = 0
disk = dict()
files = dict()
free = list()
for block in blocks:
    size = int(block[0])
    for n in range(size):
        disk[cursor+n] = file_id
    files[file_id] = cursor, size
    cursor += size
    file_id += 1
    if len(block)==2 and block[1]!='0':
        size = int(block[1])
        free.append((cursor, size))
        for n in range(size):
            disk[cursor+n] = None
        cursor += size

for file_id, (read_cursor, size) in reversed(files.items()):
    try:
        write_cursor, avail = next(f for f in free if f[1]>=size and f[0]<read_cursor)
        if avail-size:
            free[free.index((write_cursor, avail))] = (write_cursor+size, avail-size)
        else:
            free.pop(free.index((write_cursor, avail)))
        for n in range(size):
            disk[write_cursor+n] = file_id
            disk[read_cursor+n] = None
    except StopIteration:
        continue

answer = sum(position*file_id for position,file_id in disk.items() if file_id)

print("aoc 2024 day 9 part 2:", answer)
