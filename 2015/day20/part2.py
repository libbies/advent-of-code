input = int(open("input.txt").read())

presents = [0 for n in range(input//11)]

for elf in range(1, input//11):
    for n in range(1, 51):
        if n*elf >= input//11:
            break
        presents[n*elf] += elf * 11

print("len:", len(presents), "max:", max(presents))

for (i, n) in enumerate(presents):
    if n >= input:
        print(n, ">=", input, "part2:", i)
        break
