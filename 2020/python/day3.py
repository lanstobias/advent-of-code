rows = []
with open("input/day3.txt") as lines:
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        rows.append(row)

def part1(right, down):
    trees, x, y = 0, 0, 0
    while y < (len(rows)):
        if rows[y][x] == '#':
            trees += 1
        x = (x + right) % (len(rows[0]) - 1)
        y += down

    return trees

def part2():
    return part1(1,1) * part1(3,1) * part1(5,1) * part1(7,1) * part1(1,2)

print("Part 1: {}".format(part1(3, 1)))
print("Part 2: {}".format(part2()))
