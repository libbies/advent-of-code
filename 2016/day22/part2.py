lines = [l.split() for l in open("input.txt").read().splitlines() if "/" in l]

nodes = dict()
for l in lines:
    _, x, y = [s[1:] for s in l[0].split('-')]
    nodes[(int(x), int(y))] = [int(s[:-1]) for s in l[1:]]

# Filesystem              Size  Used  Avail  Use%
SIZE = 0
USED = 1
AVAIL = 2
PERCENT = 3

lx, ly = max(n[0] for n in nodes) + 1, max(n[1] for n in nodes) + 1

for x in range(4):
    for y in range(19, ly):
        print(f"{nodes[(x,y)][USED]:>3}/{nodes[(x,y)][AVAIL]:>2}", end=' ')
    print()

# solved by hand, lol

# step 1: move nodes[(3,28)] ==> nodes[(0,19)]
#[73/13] 72/17  72/19  66/23  71/14  73/18  67/22  70/19  73/14  73/20  67/23  68/21
# 71/19 492/17  69/21  65/29  65/27  70/22  64/27  65/22  68/26  69/18  71/19  70/24
# 66/22 494/12  64/27  65/27  67/23  73/20  68/24  73/21  69/16  69/19  68/17  73/13
# 72/18 497/11  70/21  67/20  70/16  67/23  65/25  64/23  72/13 [ 0/88] 71/19  73/14
# (3,28) - (0,19) = 12 steps

# step 2: move nodes[(0,19)] ==> nodes[(0,0)]
# (0,19) - (0,0) = 19 steps

# step 3: move nodes[(0,0)] ==> nodes[(32,0)]
# (32,0) - (0,0) = 32 steps

for x in range(lx-5, lx):
    print(f"{x:>2}", end='')
    for y in range(2):
        print(f"{nodes[(x,y)][USED]:>3}/{nodes[(x,y)][AVAIL]:>2}", end=' ')
    print()

# step 4: nodes[(31,0)] ==> nodes[(0,0)]
# 28: 72/22  68/26
# 29: 71/14  71/20
# 30: 66/19v<65/27 # right, up, up, left, down
# 31: 71/18 ^73/17 # five moves to shift the blank space up once
# 32: 70/19>^72/15
# (31,0) - (0,0) = 31 steps * 5 moves per step = 155

print("lol part2:", 12 + 19 + 32 + 155)
