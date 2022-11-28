from functools import lru_cache

state = open("input.txt").read().strip()

@lru_cache(maxsize=256)
def check(s):
    tmp = ''
    for n in range(0, len(s), 2):
        if s[n:n+2] in ('00', '11'):
            tmp += '1'
        else:
            tmp += '0'
    return tmp

size = 35651584
while len(state) < size:
    a = state
    b = state[::-1].replace('1', '#').replace('0', '1').replace('#', '0')
    state = a + '0' + b

blocksize = 1024
checksum = state[:size]
iterations = 0
while len(checksum) % 2 == 0:
    # print(iterations, len(checksum))
    tmp = ''
    for n in range(0, len(checksum), blocksize):
        tmp += check(checksum[n:n+blocksize])
    iterations += 1
    checksum = tmp

print(check.cache_info())
print(iterations, "iterations, part1:", checksum)
