horizontal = depth = aim = 0

with open("input/day2.txt") as infile:
    for line in infile:
        coordinate = line.split()
        direction = coordinate[0]
        steps = int(coordinate[1])

        if direction == 'forward':
            horizontal += steps
            depth += (aim * steps)
        if (direction == 'up'):
            aim -= steps
        if (direction == 'down'):
            aim += steps

print(horizontal * depth)

