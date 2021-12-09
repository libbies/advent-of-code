from pprint import pprint
from copy import deepcopy

input = open("input.txt").read().replace('.', ' ').replace('#', '█').splitlines()

slice = [None] * len(input)
for i, row in enumerate(input):
    slice[i] = list(row)

slices = [slice]

for iteration in range(6):
    # add padding for cols
    for i, slice in enumerate(slices):
        for j, row in enumerate(slice):
            slices[i][j] = [' ', ' '] + row + [' ', ' ']
        slices[i] = ([[' ']*len(slices[i][j])]
                     + [[' ']*len(slices[i][j])]
                     + slices[i]
                     + [[' ']*len(slices[i][j])]
                     + [[' ']*len(slices[i][j])])

    # add pading for rows
    tmp = [None] * len(slices[0])
    for i, row in enumerate(slices[0]):
        tmp[i] = [' ' for c in row]
    slices = [deepcopy(tmp)] + [deepcopy(tmp)] + slices + [deepcopy(tmp)] + [deepcopy(tmp)]

    # toggle cubes
    state = deepcopy(slices)
    for i, slice in enumerate(slices[:-1]):
        if i == 0:
            continue
        for j, row in enumerate(slice[:-1]):
            if j == 0:
                continue
            for k, cube in enumerate(row[:-1]):
                if k == 0:
                    continue
                cubes = list()
                for z in (i-1, i, i+1):
                    for x in (j-1, j, j+1):
                        for y in (k-1, k, k+1):
                            cubes.append(slices[z][x][y])
                if slices[i][j][k] == ' ' and cubes.count('█') == 3:
                    state[i][j][k] = '█'
                if slices[i][j][k] == '█' and cubes.count('█') not in (3, 4):
                    state[i][j][k] = ' '

    slices = deepcopy(state)
    count = 0
    for i, slice in enumerate(slices):
        for j, row in enumerate(slice):
            # print(i,j, row)
            count += row.count('█')

print(iteration+1, "iterations, part1:", count)
