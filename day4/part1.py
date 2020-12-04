print(len([
    p for p in [
        {l.split(':')[0]: l.split(':')[1]  for l in line}
        for line in [*map(str.split, open("input.txt").read().split('\n\n'))]
    ]
    if len(p)>=7
    if not(len(p)<8 and "cid" in p)
]))
