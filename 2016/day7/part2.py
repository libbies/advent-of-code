import re

addresses = open("input.txt").read().splitlines()

def get_bab(s):
    l = len(s)
    babs = list()
    for n in range(l-2):
        if s[n] == s[n+2] and s[n] != s[n+1]:
            babs.append(s[n:n+3])
    return babs

valid = 0
for addr in addresses:
    hypernets = re.findall('\[[^\]]+\]', addr)
    babs = list()
    for net in hypernets:
        babs += get_bab(net)
        addr = addr.replace(net, '|')
    if not babs:
        continue
    for bab in babs:
        aba = bab[1:] + bab[1]
        if aba in addr:
            # print(bab, aba, addr)
            valid += 1
            break

print("part2:", valid)
