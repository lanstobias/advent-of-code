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
    counter = 0
    prev_sum = -1

    for i, value in enumerate(values):
        if len(values) <= (i + 2):
            return counter

        summ = values[i] + values[i+1] + values[i+2]

        if summ > prev_sum:
            if prev_sum >= 0:
                counter += 1

        prev_sum = summ

print('Part 2: {}'.format(part2()))

