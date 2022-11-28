#!/usr/bin/env python3
import sys, numpy

def render(canvas):
    (height, width) = canvas.shape
    for x in range(height):
        print('█', end='')
        for y in range(width):
            cell = canvas[x,y]
            # 0 = black
            # 1 = white
            # 2 = transparent
            if cell == 0:
                print('█', end='')
            if cell == 1:
                print(' ', end='')
        print('█')


def main(argv=sys.argv):
    verbose = False
    if "-v" in argv:
        verbose = True
    if len(argv) <= 3:
        raise(IndexError)
    width = int(argv[-3])
    height = int(argv[-2])
    f = argv[-1]

    pixels = [int(pixel) for pixel in open(f, 'r').read().strip()]
    nlayers = len(pixels) // (width*height)

    print(f"read {len(pixels)} pixels with {nlayers} layers of {width*height} pixels per layer")

    layers = list()
    for n in range(nlayers):
        layers.append(list())
        for _ in range(width*height):
            layers[n].append(pixels.pop(0))

    zeros = dict()
    for n in range(nlayers):
       zeros[n] = len([0 for _ in layers[n] if _ == 0])

    # checksum
    minlayer = min(zeros, key=zeros.get)
    ones = [1 for _ in layers[minlayer] if _ == 1]
    twos = [2 for _ in layers[minlayer] if _ == 2]
    print(f"checksum is {len(ones) * len(twos)}")

    canvas = numpy.zeros([height, width], dtype=int)
    for layer in layers[::-1]:
        # print(layer)
        for x in range(height):
            for y in range(width):
                cell = layer[(x*width)+y]
                # 0 = black
                # 1 = white
                # 2 = transparent
                if cell == 2:
                    continue
                else:
                    canvas[x, y] = cell 
        if verbose:
            print(canvas)
            render(canvas)
    print(canvas)
    render(canvas)

if __name__ == "__main__":
    main()
