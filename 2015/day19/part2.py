# import code

lines = open("input.txt").read().splitlines()

molecule = lines[-1]

subs = dict()
for l in lines:
    if '=>' not in l:
        continue
    l = l.split()
    if l[-1] in subs:
        raise RuntimeError # FIXME
    subs[l[-1]] = l[0]

iterations = 1
working_set = {molecule}
while working_set:
    tmp = list()
    for mol in working_set:
        for sub in subs:
            if subs[sub] == "e" and len(mol) > 3:
                break
            l = len(sub)
            for n in range(l, len(mol)+1):
                if mol[n-l:n] == sub:
                    tmp.append(mol[:n-l] + subs[sub] + mol[n:])
    min_len = min(len(m) for m in tmp)
    magic = 1 # number of candidates to pass to next iteration
    tmp = [m for m in tmp if len(m)==min_len][:magic]
    if iterations % 20 == 0:
        print(iterations, '=>', len(tmp), "item(s), len:", min_len)
    if 'e' in tmp:
        print("part2:", iterations)
        break
    iterations += 1
    working_set = set(tmp)
    # code.interact(local=dict(globals(), **locals()))
