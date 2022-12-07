#!python
"""advent of code 2022 day 7 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

path = list()
root = dict()
for line in lines:
    if line[0] == '$': # cmd
        if line[1] == "cd":
            if line[-1] == '/':
                path = [ ]
            elif line[-1] == "..":
                _ = path.pop()
            else: # folder
                path.append(line[-1])
    elif line[0] == "dir": # directory
        dir = root
        for p in path:
            dir = dir[p]
        dir[line[1]] = dict()
    else: # file
        dir = root
        for p in path:
            dir = dir[p]
        dir[line[1]] = int(line[0])

def check_size(dir):
    size = 0
    for subdir in (d for d in dir.values() if type(d)==dict):
        size += check_size(subdir)
    size += sum(f if type(f)==int else 0 for f in dir.values())
    return size

def recurse_dirs(dir):
    size = 0
    for subdir in (d for d in dir.values() if type(d)==dict):
        if check_size(subdir) <= 100000:
            size += check_size(subdir)
        size += recurse_dirs(subdir)
    return size

answer = recurse_dirs(root)

print("part 1:", answer)
