import code
from collections import deque

class queue(deque):
    def __init__(self, iterable=None):
        super().__init__(iterable)
        self.inserts = dict()
    def qpop(self):
        p = self.pop()
        if p in self.inserts:
            self.append(p)
            for c in self.inserts[p]:
                self.append(c)
            del self.inserts[p]
            return self.pop()
        return p
    def qpopleft(self):
        p = self.popleft()
        if p in self.inserts:
            for c in reversed(self.inserts[p]):
                self.appendleft(c)
            del self.inserts[p]
        return p
    def qindex(self, item):
        if item not in self:
            k = next((k for k, v in self.inserts.items() if item in v), None)
            i = self.qindex(k)
            for c in reversed(self.inserts[k]):
                self.insert(i+1, c)
        return self.index(item)

cups = queue(map(int, open("input.txt").read().strip())) + queue(range(10, 1000001))

m = max(cups)
move = 1
while move <= 10000000:
    label = cups.qpopleft()
    cups.append(label)
    pickup = deque(cups.qpopleft() for n in range(3))
    dst = label
    while True:
        dst -= 1
        if dst <= 0:
            dst = next(n for n in range(m, m-4, -1) if n not in pickup)
        elif dst in pickup:
            continue
        cups.inserts[dst] = pickup
        break
    if move % 1000000 == 0:
        print(f"mv:{move:>8}, len(cups): {len(cups)} + {len(cups.inserts)*3}"
              f" = {len(cups)+len(cups.inserts)*3}, {dst:>6}: {pickup}")
    move += 1

answer = list()

if 1 not in cups:
    print("1 not found, inserting...")
    print("...done, qidx =", cups.qindex(1))

if 1 in cups.inserts:
    answer += cups.inserts[1]
elif 1 in cups:
    answer.append(cups[(cups.index(1)+1)%len(cups)])
    answer.append(cups[(cups.index(1)+2)%len(cups)])

if answer[0] in cups.inserts:
    print("part2:", answer[0] * cups.inserts[answer[0]][0])
else:
    print("part2:", answer[0] * answer[1])

# code.interact(local=dict(globals(), **locals()))
