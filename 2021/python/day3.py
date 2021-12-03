from collections import defaultdict

def readlines(filename):
    lines = []
    with open(filename) as infile:
        for line in infile:
            lines.append(line.strip())
    return lines

values = readlines('input/day3.txt')

def part1():
    gamma = []
    epsilon = []

    for col in range(len(values[0])):
        one = zero = 0
        for row in range(len(values)):
            if (values[row][col]) == '1':
                one += 1
            else:
                zero += 1

        if one > zero:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    gamma_dec = int(''.join(str(bit) for bit in gamma), 2)
    epsilon_dec = int(''.join(str(bit) for bit in epsilon), 2)

    return gamma_dec * epsilon_dec

print(part1())

