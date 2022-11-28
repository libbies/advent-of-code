from collections import deque

number = deque(open("input.txt").read().strip())

for i in range(1, 41):
    count = 1
    letter = number.popleft()
    result = str()
    for next_letter in number:
        if letter == next_letter:
            count += 1
        else:
            result += str(count) + letter
            letter = next_letter
            count = 1
    if not result or result[-1] != letter:
        result += str(count) + letter
    number = deque(result)

print(i, "iterations, part1:", len(result))

for i in range(41, 51):
    count = 1
    letter = number.popleft()
    result = str()
    for next_letter in number:
        if letter == next_letter:
            count += 1
        else:
            result += str(count) + letter
            letter = next_letter
            count = 1
    if result[-1] != letter:
        result += str(count) + letter
    number = deque(result)
    # print(i, "iterations:", len(result))

print(i, "iterations, part2:", len(result))
