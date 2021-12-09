input = open("input.txt").read().splitlines()

timestamp = int(input[0])
buses = input[1].split(',')

schedule = dict()
for bus in [int(b) for b in buses if b!='x']:
    # print(f"{timestamp}, {bus}, {((1+(timestamp//bus)) * bus)%timestamp}")
    schedule[bus] = ((1+(timestamp//bus)) * bus)%timestamp

result = sorted(schedule.items(), key=lambda x: x[1])[0]
print(f"part1:", result[0] * result[1])
