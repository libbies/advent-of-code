inputs = map(str.split, open("input.txt").read().splitlines())

mem = dict()
for addr, _, val  in inputs:
    if addr == "mask":
        mask, l = val, len(val)
    if addr.startswith("mem"):
        val = bin(int(val))[2:].zfill(l)
        mem[addr] = int(''.join([
                mask[n] if mask[n]!='X' else val[n] for n in range(l)
            ]),2)

print("part1:", sum(mem.values()))
