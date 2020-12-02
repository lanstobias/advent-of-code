valid_passwords_part1 = 0
valid_passwords_part2 = 0

with open("input/day2.txt") as lines:
    for line in lines:
        condition, password = line.split(':')[0], line.split(':')[1]
        condition, letter = condition[:-2], condition[-1]
        low, high = [int(n) for n in condition.split('-')]

        if (low <= password.count(letter) <= high):
            valid_passwords_part1 += 1

        if ((password[low] == letter) ^ (password[high] == letter)):
            valid_passwords_part2 += 1

print("Part 1: {}".format(valid_passwords_part1))
print("Part 2: {}".format(valid_passwords_part2))
