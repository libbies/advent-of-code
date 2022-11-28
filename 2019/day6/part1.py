#!/usr/bin/env python3
import sys
from collections import defaultdict

def count_orbits(orbital_map, body, n=0):
    if body in orbital_map:
        return 1 + count_orbits(orbital_map, orbital_map[body], n)
    else:
        return n

def main(argv=sys.argv):
    verbose = False
    if "-v" in argv:
        verbose = True
    f = argv[-1]

    orbits = [o.strip() for o in open(f, 'r').readlines()]
    print(f"loaded {len(orbits)} orbits")

    orbital_map = defaultdict(list)
    for orbit in orbits:
        primary, secondary = orbit.split(')')
        orbital_map[secondary] = primary

    total = 0
    for key, value in orbital_map.items():
        if verbose:
            print(key, value, count_orbits(orbital_map, key))
        total += count_orbits(orbital_map, key)
    print(f"total: {total}")

if __name__ == "__main__":
    main()
