#!python
"""advent of code 2022 day 7 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

path = list()
root = dict()
cwd = root
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

def check_size(dir):
    size = 0
    for subdir in [_ for _ in dir.values() if type(_)==dict]:
        size += check_size(subdir)
    size += sum(_ if type(_)==int else 0 for _ in dir.values())
    return size

def recurse_dirs(dir):
    size = 0
    for subdir in [_ for _ in dir.values() if type(_)==dict]:
        if check_size(subdir) < 100000:
            size += check_size(subdir)
        size += recurse_dirs(subdir)
    return size

answer = recurse_dirs(root)

print("part 1:", answer)
