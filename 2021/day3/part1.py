"""advent of code 2021 day 3 part 1"""
inputs = open("input.txt").read().splitlines()

gamma = ""
epsilon = ""
for i in range(len(inputs[0])):
    bits = [_[i] for _ in inputs]
    gamma += max(set(bits), key=bits.count)
    epsilon += min(set(bits), key=bits.count)

answer = int("0b"+gamma, 2) * int("0b"+epsilon, 2)
print("part 1 answer:", answer)
