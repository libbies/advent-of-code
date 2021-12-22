#!python
"""advent of code 2021 day 22 part 2"""
lines = open("input.txt").read().splitlines()

cuboids = []
for line in lines:
    op, cuboid = line.split()
    x, y, z = cuboid.split(',')
    x = sorted((int(x.split('=')[-1].split('.')[0]), int(x.split('=')[-1].split('.')[-1])))
    y = sorted((int(y.split('=')[-1].split('.')[0]), int(y.split('=')[-1].split('.')[-1])))
    z = sorted((int(z.split('=')[-1].split('.')[0]), int(z.split('=')[-1].split('.')[-1])))
    cuboids.append((op, (x,y,z)))

def get_intersection(cube_a, cube_b):
    (ax, ay, az), (bx, by, bz) = cube_a, cube_b
    if max(ax)<min(bx) or max(bx)<min(ax) \
            or max(ay)<min(by) or max(by)<min(ay) \
            or max(az)<min(bz) or max(bz)<min(az):
        return None
    return ((max((min(ax), min(bx))), min((max(ax), max(bx)))),
            (max((min(ay), min(by))), min((max(ay), max(by)))),
            (max((min(az), min(bz))), min((max(az), max(bz)))))

def get_volume(cube):
    x, y, z = cube
    return (max(x)-min(x)+1) * (max(y)-min(y)+1) * (max(z)-min(z)+1)

intersects = []
while cuboids:
    op, (x, y, z) = cuboids.pop(0)
    for prev, (px, py, pz) in list(intersects):
        intersect = get_intersection((x,y,z), (px,py,pz))
        if intersect:
            if prev=="on":
                intersects.append(("off", intersect))
            elif prev=="off":
                intersects.append(("on", intersect))
    if op=="on":
        intersects.append(("on", (x,y,z)))

volume = 0
for op, cuboid in intersects:
    if op=="on":
        volume += get_volume(cuboid)
    else:
        volume -= get_volume(cuboid)

answer = volume
print("aoc 2021 day 22 part 2:", answer)
