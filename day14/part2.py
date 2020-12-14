inputs = [*map(str.split, open("input.txt").read().splitlines())]

mem = dict()
for addr, _, val  in inputs:
    if addr == "mask":
        mask, l = val, len(val)
    if addr.startswith("mem"):
        addr = bin(int(addr[4:-1]))[2:].zfill(l)
        addrs = [str()]
        for n in range(l):
            if mask[n] == '0':
                addrs = [a+addr[n] for a in addrs]
            if mask[n] == '1':
                addrs = [a+'1' for a in addrs]
            if mask[n] == 'X':
                addrs = [a+x for a in addrs for x in ('0', '1')]
        for addr in addrs:
            mem[addr] = int(val)

print("part2", sum(mem.values()))
