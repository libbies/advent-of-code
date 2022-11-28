#!/usr/bin/env python3
import sys
from collections import defaultdict

def count_orbits(orbital_map, body, n=0):
    if body in orbital_map:
        return 1 + count_orbits(orbital_map, orbital_map[body], n)
    else:
        return n

def count_distance(orbital_map, transits, orbiting_body, target_body, n=0, verbose=False):
    if verbose:
        print(f"o:{orbiting_body} t:{target_body} transits:{transits}")

    if (target_body == orbital_map[orbiting_body] or orbiting_body == orbital_map[target_body]):
        return (True, 0)

    for next_body in (([orbital_map[orbiting_body]] if orbiting_body in orbital_map else [])
            + [p for (p, s) in orbital_map.items() if s == orbiting_body if p and p != orbiting_body]):
        if not next_body or next_body in transits:
            continue
        else:
            transits += [next_body]
            found, distance = count_distance(orbital_map, transits, next_body, target_body, verbose=verbose)
        if found:
            return (True, distance + 1)
        else:
            _ = transits.pop(-1)
            continue

    return (False, 0)

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
        total += count_orbits(orbital_map, key)
    print(f"total: {total} orbits")

    target = "SAN"
    transits = list()
    found, distance = count_distance(orbital_map, transits, orbital_map["YOU"], target, verbose=verbose)
    print(f"distance to {target}: {distance}")

if __name__ == "__main__":
    main()
