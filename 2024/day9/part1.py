#!/usr/bin/env python3
"""advent of code 2024 day 9 part 1"""

diskmap = open("input.txt").read().strip()
blocks = iter(diskmap[i:i+2] for i in range(0, len(diskmap), 2))

cursor = 0
file_id = 0
disk = dict()
for block in blocks:
    size = int(block[0])
    for n in range(size):
        disk[cursor+n] = file_id
    cursor += size
    file_id += 1
    if len(block)==2 and block[1]!='0':
        size = int(block[1])
        for n in range(size):
            disk[cursor+n] = None
        cursor += size

write_cursor, read_cursor = 0, len(disk)-1
while write_cursor < read_cursor:
    while disk[read_cursor] is None:
        read_cursor -= 1
    while disk[write_cursor] is not None:
        write_cursor += 1
    if write_cursor>=read_cursor:
        break
    disk[write_cursor] = disk[read_cursor]
    disk[read_cursor] = None

answer = sum(position*file_id for position,file_id in disk.items() if file_id)

print("aoc 2024 day 9 part 1:", answer)
