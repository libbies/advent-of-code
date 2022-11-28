#!/usr/bin/env python3
import sys

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

    minlayer = min(zeros, key=zeros.get) 
    ones = [1 for _ in layers[minlayer] if _ == 1]
    twos = [2 for _ in layers[minlayer] if _ == 2]
    print(len(ones) * len(twos))

if __name__ == "__main__":
    main()
