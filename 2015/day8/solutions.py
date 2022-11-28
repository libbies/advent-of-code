lines = open("example.txt").read().splitlines()

bytes = sum([len(l) for l in lines])

characters = 0
for line in lines:
    characters += len(str(eval(line)))

print(f"{bytes}-{characters}=part1: {bytes-characters}")

characters = 0
for line in lines:
    characters += len(line) + line.count(chr(92)) + line.count(chr(34)) + 2

print(f"{characters}-{bytes}=part2: {characters-bytes}")
