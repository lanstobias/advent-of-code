def readlines(filename):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(int(line))
    return lines

values = readlines('input/day1.txt')

def part1():
    counter = 0
    previous_value = values[0]
    for value in values:
        if value > previous_value:
            counter += 1
        previous_value = value

    return counter

print('Part 1: {}'.format(part1()))

def part2():
    i = 0

    # Check if end
    if len(i + 2) > values:
        return

    if (values[i] and values)

print('Part 1: {}'.format(part1()))

