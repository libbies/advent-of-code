#!python
"""advent of code 2022 day 7 part 1"""
lines = [line.split() for line in open("input.txt").read().splitlines()]

path = list()
root = dict()
for line in lines:
    if line[0] == '$': # cmd
        if line[1] == "cd":
            if line[-1] == '/': # cd /
                path = [ ]
            elif line[-1] == "..": # cd ..
                _ = path.pop()
            else: # cd <dir>
                path.append(line[-1])
            cwd = root
            for p in path:
                cwd = cwd[p]
    elif line[0] == "dir": # directory
        cwd[line[1]] = dict()
    else: # file
        cwd[line[1]] = int(line[0])

def get_size(directory):
    size = 0
    for subdir in (d for d in directory.values() if type(d)==dict):
        size += get_size(subdir)
    size += sum(f if type(f)==int else 0 for f in directory.values())
    return size

def recurse_dirs(directory):
    size = 0
    for subdir in (d for d in directory.values() if type(d)==dict):
        if get_size(subdir) <= 100_000:
            size += get_size(subdir)
        size += recurse_dirs(subdir)
    return size

answer = recurse_dirs(root)

print("part 1:", answer)
