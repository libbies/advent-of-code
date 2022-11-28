lines = open("input.txt").read().splitlines()

molecule = lines[-1]

substitutions = dict()
for l in lines:
    if '=>' not in l:
        continue
    l = l.split()
    if l[0] in substitutions:
        substitutions[l[0]].append(l[-1])
    else:
        substitutions[l[0]] = [l[-1]]

molecules = set()
for sub in substitutions:
    l = len(sub)
    for n in range(l, len(molecule)+1):
        if molecule[n-l:n] == sub:
            for s in substitutions[sub]:
                molecules.add(molecule[:n-l] + s + molecule[n:])

print("part1:", len(molecules))
