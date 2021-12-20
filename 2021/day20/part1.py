#!python
"""advent of code 2021 day 10 part 1"""
from collections import defaultdict

def bounds(img):
    """get the bounds of the slice of our infinite image"""
    return (min(img.keys()),
            max(image.keys()),
            min(k for row in img.values() for k in row),
            max(k for row in img.values() for k in row),)

def fill_edges(img, pixel):
    x_min, x_max, y_min, y_max = bounds(img)
    for x in (x_min-1, x_max+1):
        img[x] = dict()
        for y in range(y_min-1, y_max+2):
            img[x][y] = pixel
    for x in range(x_min-1, x_max+2):
        for y in (y_min-1, y_max+1):
            img[x][y] = pixel

def count(img):
    result = 0
    for row in sorted(img.keys()):
        for col in img[row].keys():
            result += img[row][col]
    return result

def print_image(img, width=10):
    print('\n'.join(''.join(str(img[x][y])
                    for y in sorted(img[x])[:width])
                    for x in sorted(img.keys())[:width]))
    print()

lines = open("input.txt").read().splitlines()
algorithm = [int(c) for c in lines[0].replace('.', '0').replace('#', '1')]
image = defaultdict(lambda:defaultdict(int))
for i, r in enumerate(lines[2:]):
    for j, p in enumerate(r):
        image[i][j] = 0 if p=='.' else 1

image = {k:dict(v) for k,v in image.items()}
step = 0
limit = 2
print(f"pass 0/{limit}:")
print_image(image)
fill_edges(image, 0)
while step<limit:
    step += 1
    print(f"pass {step}/{limit}:")
    edge = image[min(image.keys())][0]
    fill_edges(image, edge)
    result = {x:{y:0 for y in image[x].keys()} for x in image.keys()}
    fill_edges(image, edge)
    x_min, x_max, y_min, y_max = bounds(image)
    for x in range(x_min+1, x_max):
        for y in range(y_min+1, y_max):
            result[x][y] = algorithm[int("0b" + ''.join(str(image[x+dx][y+dy])
                                            for dx in (-1,0,1)
                                            for dy in (-1,0,1)), 2)]
    print(f"bounds: {bounds(result)}, result:")
    print_image(result)
    image = result

answer = count(image)
print("aoc 2021 day 20 part 1:", answer)
