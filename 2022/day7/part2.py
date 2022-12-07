#!python
"""advent of code 2022 day 7 part 2"""
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

sizes = dict()
def get_size(directory):
    size = 0
    for name, subdir in ((name,d) for (name,d) in directory.items() if type(d)==dict):
        sizes[name] = get_size(subdir)
        size += sizes[name]
    size += sum(f if type(f)==int else 0 for f in directory.values())
    return size

free_space   = 70_000_000 - get_size(root)
space_needed = 30_000_000 - free_space

for s in sorted(sizes.values()):
    if s >= space_needed:
        answer = s
        break

print("part 2:", answer)
