"""advent of code 2021 day 12 part 2"""
lines = [_.split('-') for _ in open("example3.txt").read().splitlines()]
caves = {c:False for line in lines for c in line if c!="start"}

paths = dict()
for c1,c2 in lines:
    if c1 not in paths and c2!="start":
        paths[c1] = [c2]
    elif c2!="start" and c2 not in paths[c1]:
        paths[c1].append(c2)
    if c2 not in paths and c1!="start":
        paths[c2] = [c1]
    elif c1!="start" and c1 not in paths[c2]:
        paths[c2].append(c1)

deadends = set()
_ = paths.pop("end")
loc = "start"
path, completed = ["start"], []
while path:
    l = len(path)
    candidates = paths[loc]
    if "end" in candidates and path+["end"] not in completed:
        completed.append(path+["end"])
    counts = [path.count(p) for p in path if p.islower()]
    for c in candidates:
        if c in ["start", "end"]:
            continue
        if c.islower() and c in path and 2 in counts:
            continue
        if tuple(path+[c]) in deadends:
            continue
        path.append(c)
        loc = c
        break
    else:
        deadends.add(tuple(path))
        if path.pop()=="start":
            break
        loc = path[-1]

answer = len(completed)
print("aoc 2021 day 12 part 2:", answer)
