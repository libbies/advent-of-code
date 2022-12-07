#!python
"""advent of code 2022 day 7 part 2"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

path = list()
root = dict()
for line in lines:
    if line[0] == '$': # cmd
        if line[1] == "cd":
            if line[-1] == "/":
                path = [ ]
            elif line[-1] == "..":
                _ = path.pop()
            else: # folder
                dir = root
                for p in path:
                    dir = dir[p]
                path.append(line[-1])
    elif line[0] == "dir": # directory
        dir = root
        for p in path:
            dir = dir[p]
        if line[1] not in dir:
            dir[line[1]] = dict()
    else: # file
        dir = root
        for p in path:
            dir = dir[p]
        if line[1] not in dir:
            dir[line[1]] = int(line[0])

sizes = dict()
def check_size(dir):
    size = 0
    for name, subdir in [(k,v) for (k,v) in dir.items() if type(v)==dict]:
        size += check_size(subdir)
        sizes[name] = check_size(subdir)
    size += sum([_ if type(_)==int else 0 for _ in dir.values()])
    return size

free_space = 70000000 - check_size(root)
space_needed = 30000000 - free_space

for s in sorted(sizes.values()):
    if s >= space_needed:
        answer = s
        break

print("part 2:", answer)
