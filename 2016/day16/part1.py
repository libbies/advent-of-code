state = open("input.txt").read().strip()

size = 272

while len(state) < size:
    a = state
    b = state[::-1].replace('1', '#').replace('0', '1').replace('#', '0')
    state = a + '0' + b

checksum = str()
iterations = 0
while not checksum or len(checksum) % 2 == 0:
    if not checksum:
        checksum = state[:size]
    # print(iterations, checksum)
    tmp = ''
    for n in range(0, len(checksum), 2):
        if checksum[n:n+2] in ['00', '11']:
            tmp += '1'
        else:
            tmp += '0'
    iterations += 1
    checksum = tmp

print(iterations, "iterations, part1:", checksum)
