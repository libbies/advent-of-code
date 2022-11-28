import random
from collections import deque

inserts = dict()

def qpopleft(q):
    p = q.popleft()
    if p in inserts:
        q.extendleft(reversed(inserts[p]))
        del inserts[p]
    return p

def qindex(q, item):
    if item not in q:
        k = next((k for k, v in inserts.items() if item in v), None)
        i = qindex(q, k)
        for c in reversed(inserts[k]):
            q.insert(i+1, c)
        del inserts[k]
    return q.index(item)

cups = deque(map(int, open("input.txt").read().strip())) + deque(range(10, 1_000_001))

m = max(cups)
move = 1
while move <= 10_000_000:
    label = qpopleft(cups)
    cups.append(label)
    pickup = deque(qpopleft(cups) for n in range(3))
    dst = label
    while True:
        dst -= 1
        if dst <= 0:
            dst = next(n for n in range(m, m-4, -1) if n not in pickup)
        elif dst in pickup:
            continue
        inserts[dst] = pickup
        break
    if move % 1000000 == 0:
        print(f"mv:{move:>8}, len(cups): {len(cups)} + {len(inserts)*3}"
              f" = {len(cups)+len(inserts)*3}, {dst:>6}: {pickup}")
    move += 1

answer = list()

if 1 not in cups and 1 not in inserts:
    print("1 not found, inserting...")
    print("...done, qidx =", qindex(cups, 1))

if 1 in inserts:
    answer += inserts[1]
elif 1 in cups:
    answer.append(cups[(cups.index(1)+1)%len(cups)])
    answer.append(cups[(cups.index(1)+2)%len(cups)])

if answer[0] in inserts:
    print("part2:", answer[0] * inserts[answer[0]][0])
else:
    print("part2:", answer[0] * answer[1])

# code.interact(local=dict(globals(), **locals()))
