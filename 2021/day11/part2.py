"""advent of code 2021 day 11 part 2"""
grid = {
    (x,y): int(octopus)
    for x, line in enumerate(open("input.txt").read().splitlines())
    for y, octopus in enumerate(line)
}

answer = 0
step = 0
while not answer:
    step += 1
    for x in range(10):
        for y in range(10):
            grid[(x,y)] += 1
    flashes = [(x,y) for (x,y), octopus in grid.items() if octopus>=10]
    while flashes:
        for x, y in flashes:
            grid[(x,y)] = 0
            for n in (+1, 0, -1):
                for m in (+1, 0, -1):
                    if (x+n,y+m) in grid and grid[(x+n,y+m)]>0:
                        grid[(x+n,y+m)] += 1
        flashes = [(x,y) for (x,y), octopus in grid.items() if octopus>=10]
    if sum(grid.values())==0:
        answer = step

print("aoc 2021 day 11 part 2:", answer)
