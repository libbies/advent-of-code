# part 1
print("part1:", max([int(str.translate(p,str.maketrans('FBLR','0101')),2) for p in open("input.txt").read().splitlines()]))

# part 2
print("part2:", [[*set(range(min(s), max(s)))-set(s)][0] for s in [[int(str.translate(p,str.maketrans('FBLR','0101')),2) for p in open("input.txt").read().splitlines()]]][0])
