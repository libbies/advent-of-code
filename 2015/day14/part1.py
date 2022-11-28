lines = open("input.txt").read().splitlines()

speeds = dict()
for line in lines:
    l = line.split()
    speeds[l[0]] = (int(l[3]), int(l[6]), int(l[-2]))

SPEED = 0
DURATION = 1
COOLDOWN = 2
timers = {reindeer: speeds[reindeer][DURATION] for reindeer in speeds}
distance = {reindeer: 0 for reindeer in speeds}
for n in range(1, 2504):
    for reindeer in speeds:
        if speeds[reindeer][DURATION] >= timers[reindeer]:
            distance[reindeer] += speeds[reindeer][SPEED]
        timers[reindeer] -= 1
        if timers[reindeer] == 0:
            timers[reindeer] = speeds[reindeer][COOLDOWN] + speeds[reindeer][DURATION]
    if n >= 2494:
        print("turn", n, sorted(distance.items(), key=lambda x: -x[1])[:3])

print("part1:", max(distance.values()))
