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

sizes = dict()
def check_size(dir):
    size = 0
    for name, subdir in ((name,d) for (name,d) in dir.items() if type(d)==dict):
        sizes[name] = check_size(subdir)
        size += sizes[name]
    size += sum(f if type(f)==int else 0 for f in dir.values())
    return size

free_space = 70000000 - check_size(root)
space_needed = 30000000 - free_space

for s in sorted(sizes.values()):
    if s >= space_needed:
        answer = s
        break

print("part 2:", answer)
