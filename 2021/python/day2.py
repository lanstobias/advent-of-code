def read_values(filename):
    values = []
    with open(filename) as infile:
        for line in infile:
            values.append(line.split())
    return values

coordinates = read_values('input/day2.txt')

def part1():
    horizontal = 0
    depth = 0
    aim = 0
    for coordinate in coordinates:
        direction = coordinate[0]
        steps = int(coordinate[1])
        if direction == 'forward':
            horizontal += steps
            depth += (aim * steps)
        if (direction == 'up'):
            aim -= steps
        if (direction == 'down'):
            aim += steps

        print(horizontal, aim, depth)

    return horizontal * depth

print('Part 1: {}'.format(part1()))

