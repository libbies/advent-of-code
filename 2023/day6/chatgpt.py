#!/usr/bin/env python
"""advent of code 2023 day 6 part 2
... after I asked chatgpt to speed up my solution"""

def find_valid_n_range(time, distance):
    # Solve the quadratic inequality -n^2 + time*n > distance
    root1 = (time - (time**2 - 4*distance)**0.5) / 2
    root2 = (time + (time**2 - 4*distance)**0.5) / 2

    # Find the nearest integer solutions within the range
    first = int(root1) + 1 if root1 % 1 != 0 else int(root1)
    last = int(root2)

    # Ensure that first and last are within the range and valid
    if first < 0 or first >= time or last < 0 or last >= time or last < first:
        return 0

    return last - first + 1

# Read the input file
lines = open("input.txt").readlines()

# Convert the first and last lines to integers
time = int(''.join(c for c in lines[0] if c.isnumeric()))
distance = int(''.join(c for c in lines[-1] if c.isnumeric()))

# Calculate the answer
answer = find_valid_n_range(time, distance)

# Print the answer
print("aoc 2023 day 6 part 2:", answer)
