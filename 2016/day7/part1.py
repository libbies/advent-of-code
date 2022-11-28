import re

addresses = open("input.txt").read().splitlines()

def check(s):
    l = len(s)
    for n in range(l-3):
        if s[n] != s[n+1] and s[n:n+4] == s[n:n+4][::-1]:
            return True
    return False

valid = 0
for addr in addresses:
    hypernets = re.findall('\[[^\]]+\]', addr)
    for net in hypernets:
        if check(net):
            break
        addr = addr.replace(net, '|')
    else:
        for seq in addr.split('|'):
            if check(seq):
                valid += 1
                break

print("part1:", valid)
