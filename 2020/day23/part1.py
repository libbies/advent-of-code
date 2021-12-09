import code

cups = list(map(int, open("input.txt").read().strip()))

l = len(cups)
m = max(cups)
move = 1
pos = 0
while move <= 100:
    cursor = cups[pos]
    # print("mv:", move, [f"[{c}]" if i==pos else c for i, c in enumerate(cups)])
    pickup = (cups+cups[:3])[pos+1:pos+4]
    for cup in pickup:
        cups.remove(cup)
    dst = None
    target = cursor
    while dst is None:
        target -= 1
        if target <= 0:
            target = max(cups)
        if target in pickup:
            continue
        dst = cups.index(target)
    dst %= l - 3
    # print("pickup:", pickup)
    # print("dst:", next((n for i, n in enumerate(cups) if n==target)))
    cups = (cups[:dst+1] + pickup + cups[dst+1:])
    pos = cups.index(cursor) + 1
    pos %= l
    move += 1

print("part1:", ''.join(map(str, cups[cups.index(1)+1:] + cups[:cups.index(1)])))
# code.interact(local=dict(globals(), **locals()))
