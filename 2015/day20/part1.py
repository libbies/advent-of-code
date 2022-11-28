input = int(open("input.txt").read())

presents = [0 for n in range(input)]

for elf in range(1, input):
    for n in range(1, input//elf):
        presents[n*elf] += elf * 10

print("len:", len(presents), ", max:", max(presents))

for (i, n) in enumerate(presents):
    if n >= input:
        print(n, ">=", input, " part1: ", i)
        break
