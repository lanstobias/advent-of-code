def get_buses():
    with open("input/day13.txt", 'r') as f:
        lines = f.readlines()

        departure = int(lines[0].strip())
        all_buses = lines[1].strip().split(',')

        buses = [int(bus) if bus.isdigit() else 1 for bus in all_buses]

        buses_stripped = [bus for bus in all_buses if bus != 'x']
        buses_stripped = list(map(int, buses_stripped))

    return departure, buses_stripped, buses

departure, buses_stripped, buses = get_buses()

def part1():
    for t in range(departure, departure + (max(buses_stripped) + 1)):
        for bus in buses_stripped:
            if (t % bus) == 0:
                return bus * (t - departure)

# https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfok4yk/
def part2():
    time = 0
    step = buses[0]
    for i in range(1, len(buses)):
        bus = buses[i]

        while ((time + i) % bus) != 0:
            time += step

        step *= bus

    return time

print(part1())
print(part2())
