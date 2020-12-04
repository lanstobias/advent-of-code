def read_passports():
    passports = []
    with open('input/day4.txt') as f:
        data = f.read()
        lines = data.split('\n\n')
        for line in lines:
            passport = []
            newline = line.replace('\n', ' ')
            passport.append(newline)
            passports.append(passport)
    return passports


def is_valid(passport):
    valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_keys = 0
    fields = passport[0].split(' ')
    for field in fields:
        info = field.split(":")
        if info[0] in valid_fields and is_info_valid(info[0], info[1]):
            valid_keys += 1
    if valid_keys == 7:
        return True
    return False


def is_info_valid(info, value):
    if info == 'byr':
        return (1920 <= int(value) <= 2020)
    elif info == 'iyr':
        return (2010 <= int(value) <= 2020)
    elif info == 'eyr':
        return (2020 <= int(value) <= 2030)
    elif info == 'hgt':
        if value[-2:] == 'cm':
            return (150 <= int(value[:-2]) <= 193)
        if value[-2:] == 'in':
            return (59 <= int(value[:-2]) <= 76)
    elif info == 'hcl':
        return (value[0] == '#' and len(value) == 7)
    elif info == 'ecl':
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return (value in valid_colors)
    elif info == 'pid':
        return (value[0].isnumeric() and len(value) == 9)
    elif info == 'cid':
        return True


valid_passports = 0
for passport in read_passports():
    if is_valid(passport):
        valid_passports += 1

print(valid_passports)
