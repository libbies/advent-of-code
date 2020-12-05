# part 1
print("part1:", max([int(str.translate(p,str.maketrans('FBLR','0101')),2) for p in [l.strip() for l in open("input.txt").readlines()]]))

# part 2
print("part2:", [[*set(range(min(s), max(s)))-set(s)][0] for s in [[int(str.translate(p,str.maketrans('FBLR','0101')),2) for p in [l.strip() for l in open("input.txt").readlines()]]]][0])
