#!/usr/bin/env python3
m = open('list.txt','r').readlines()

def fuel_for_module(n):
    base = n // 3 - 2
    s = base
    while base > 0:
        fuel = base // 3 - 2
        print(f"{fuel} fuel needed for {base} fuel")
        if fuel < 0:
            break
        s += fuel
        base = fuel
    return s

base = sum([fuel_for_module(int(n)) for n in m if n])

print(base)
