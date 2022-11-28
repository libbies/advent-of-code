lines = open("input.txt").read().splitlines()

ingredients = list()
for line in lines:
    ingredients.append(tuple(int(i.strip(',')) for i in line.split()[2::2]))

limit = 100
# written for 4 ingredients, number of loops will need to change if this differs
high_score = 0
for x in range(limit+1):
    for y in range(limit-x+1):
        for w in range(limit-x-y+1):
            z = limit-x-y-w
            score = (
                  max(x*ingredients[0][0] + y*ingredients[1][0]
                    + w*ingredients[2][0] + z*ingredients[3][0], 0)
                * max(x*ingredients[0][1] + y*ingredients[1][1]
                    + w*ingredients[2][1] + z*ingredients[3][1], 0)
                * max(x*ingredients[0][2] + y*ingredients[1][2]
                    + w*ingredients[2][2] + z*ingredients[3][2], 0)
                * max(x*ingredients[0][3] + y*ingredients[1][3]
                    + w*ingredients[2][3] + z*ingredients[3][3], 0)
            )
            if score > high_score:
                high_score = score
                # print(x, y, w, z, high_score)

print("part1:", high_score)
