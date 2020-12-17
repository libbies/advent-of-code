from pprint import pprint
from copy import deepcopy

def empty_slice(slice):
    """return an empty copy of a slice"""
    tmp = [None] * len(slice)
    for i, row in enumerate(slice):
        tmp[i] = [' '] * len(row)
    return tmp

def empty_layer(layer):
    """return an empty copy of a layer"""
    tmp = [None] * len(layer)
    for l, slice in enumerate(layer):
        tmp[l] = [None] * len(slice)
        for i, row in enumerate(slice):
            tmp[l][i] = [' '] * len(row)
    return tmp

def pad_slice(slice):
    """add padding to a slice"""
    tmp = [None] * len(slice)
    for i, row in enumerate(slice):
        tmp[i] = [' ', ' '] + row + [' ', ' ']
    tmp = ([[' ']*len(tmp[0])]
           + [[' ']*len(tmp[0])]
           + tmp
           + [[' ']*len(tmp[0])]
           + [[' ']*len(tmp[0])])
    return tmp

input = open("input.txt").read().replace('.', ' ').replace('#', '█').splitlines()

slice = [None] * len(input)
for i, row in enumerate(input):
    slice[i] = list(row)

slices = [slice]
layers = [slices]

for iteration in range(6):
    # add padding
    for w, slices in enumerate(layers):
        for z, slice in enumerate(slices):
            layers[w][z] = pad_slice(slice)
        layers[w] = ([empty_slice(layers[w][z])]
                     + [empty_slice(layers[w][z])]
                     + layers[w]
                     + [empty_slice(layers[w][z])]
                     + [empty_slice(layers[w][z])])
    layers = ([empty_layer(layers[w])]
               + [empty_layer(layers[w])]
               + layers
               + [empty_layer(layers[w])]
               + [empty_layer(layers[w])])

    # toggle cubes
    state = deepcopy(layers)
    for l, layer in enumerate(layers[:-1]):
        if l == 0:
            continue
        for i, slice in enumerate(layer[:-1]):
            if i == 0:
                continue
            for j, row in enumerate(slice[:-1]):
                if j == 0:
                    continue
                for k, cube in enumerate(row[:-1]):
                    if k == 0:
                        continue
                    cubes = list()
                    for w in (l-1, l, l+1):
                        for z in (i-1, i, i+1):
                            for x in (j-1, j, j+1):
                                for y in (k-1, k, k+1):
                                    cubes.append(layers[w][z][x][y])
                    if layers[l][i][j][k] == ' ' and cubes.count('█') == 3:
                        state[l][i][j][k] = '█'
                    if layers[l][i][j][k] == '█' and cubes.count('█') not in (3, 4):
                        state[l][i][j][k] = ' '

    layers = deepcopy(state)
    count = 0
    for l, layer in enumerate(layers):
        for i, slice in enumerate(layer):
            for j, row in enumerate(slice):
                count += row.count('█')

    # print(layers)
    print(iteration, "iterations, part1:", count)
