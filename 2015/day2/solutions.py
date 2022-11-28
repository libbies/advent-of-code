input = open("input.txt").read().splitlines()

paper, ribbon = 0, 0
for box in input:
    l, w, h = sorted(map(int, box.split('x')))
    paper += (l*w) + 2*((l*w)+(w*h)+(h*l))
    ribbon += (l+w+l+w) + (l*w*h)

print("part1:", total)
print("part2:", ribbon)
