def count_safe(iterations):
    tiles = open("input.txt").read().strip()
    tiles = '.' + tiles + '.'
    total = 0
    for i in range(iterations):
        total += tiles.count('.') - 2
        if i < 5 or i >= iterations - 5:
            print(f"{i+1:6}", tiles, tiles.count('.') - 2)
        tmp = '.'
        for n in range(1, len(tiles)-1):
            if ((('^' == tiles[n-1] == tiles[n]) and tiles[n+1] == '.')
                    or (('^' == tiles[n] == tiles[n+1]) and tiles[n-1] == '.')
                    or (('.' == tiles[n] == tiles[n+1]) and tiles[n-1] == '^')
                    or (('.' == tiles[n-1] == tiles[n]) and tiles[n+1] == '^')):
                tmp += '^'
            else:
                tmp += '.'
        tiles = tmp + '.'
    return total

print("part1:", count_safe(40))
print("part2:", count_safe(400000))
