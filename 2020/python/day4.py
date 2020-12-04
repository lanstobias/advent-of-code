import os
import re

valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = []
with open('input/day4.txt') as f:
    data = f.read()
    lines = data.split('\n\n')
    for line in lines:
        passport = []
        newline = line.replace('\n', ' ')
        passport.append(newline)
        passports.append(passport)

def is_valid(passport):
    valid_keys = 0
    print('passport: {}'.format(passport))
    fields = passport[0].split(' ')
    print('fields: {}'.format(fields))
    for field in fields:
        print('field: {}'.format(field))
        info = field.split(":")
        print('info: {}'.format(info))
        print('info[0]: {}'.format(info[0]))
        if info[0] in valid_fields and is_info_valid(info[0], info[1]):
            valid_keys += 1
            print('valid_keys: {}'.format(valid_keys))
    if valid_keys == 7:
        return True
    return False

def is_info_valid(info, value):
    if info == 'byr':
        if (1920 < int(value) < 2020):
            print('byr true')
            return True
        else:
            print('byr false')
            return False

    elif info == 'iyr':
        if (2010 <= int(value) <= 2020):
            print('iyr true')
            return True
        else:
            print('iyr false')
            print(int(value))
            return False

    elif info == 'eyr':
        if (2020 <= int(value) <= 2030):
            print('eyr true')
            return True
        else:
            print('eyr false')
            return False

    elif info == 'hgt':
        if info[:2] == 'cm':
            if (150 <= int(value) <= 193):
                print('hgt cm true')
                return True
            else:
                print('hgt cm false')
                return False

        if info[:2] == 'in':
            if (59 <= int(value) <= 76):
                print('hgt in true')
                return True
            else:
                print('hgt in false')
                return False

    elif info == 'hcl':
        if (value[0] == '#' and len(value) == 7):
            print('hcl true')
        else:
            print('hcl false')
            return False

    elif info == 'ecl':
        valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if value in valid_colors:
            print('ecl true')
            return True
        else:
            print('ecl false')
            return False

    elif info == 'pid':
        if int(value[0]) == 0 and len(value) == 9:
            print('pid true')
            return True
        else:
            print(value[0])
            print(len(value))
            print('pid false')
            return False

valid_passports = 0
for passport in passports:
    if is_valid(passport):
        valid_passports += 1
    print('-------')
print(valid_passports)