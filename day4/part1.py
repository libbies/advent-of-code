print(len([
    p for p in [
        {l.split(':')[0]: l.split(':')[1]  for l in line}
        for line in [*map(str.split, open("input.txt").read().split('\n\n'))]
    ]
    if len(p)>=7
    if len(p)>=8 or "cid" not in p
]))
