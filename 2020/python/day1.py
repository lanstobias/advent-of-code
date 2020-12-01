import tools

values = tools.readlines_int('input/day1.txt')

def part1():
    for value in values:
        for i in range(len(values)):
            if (value + values[i]) == 2020:
                return value * values[i]

def part2():
    max_value = 1500
    sorted_values = sorted(values)
    sorted_values[:] = [x for x in sorted_values if x <= max_value]
    for a in sorted_values:
        for b in sorted_values:
            for c in sorted_values:
                sum = (a + b + c)
                if sum == 2020:
                    return a * b * c


print('Part 1: {}'.format(part1()))
print('Part 2: {}'.format(part2()))

