#!/usr/bin/env python
# Solution to the AOC2020 Challenge 7/8
# https://adventofcode.com/2020/day/4

# GOAL 1: Multiline String Parsing and attr verification
# GOAL 2: Data Validation

def check_complete_passport(passport: dict, attrs):
    for key in attrs:
        if key not in passport:
            return False

    return True


def check_valid_passport(passport: dict, attrs):
    for key in attrs:
        if key not in passport:
            return False

    birth_year = int(passport['byr'])
    if not birth_year in range(1920, 2002+1):
        return False

    issue_year = int(passport['iyr'])
    if not issue_year in range(2010, 2020+1):
        return False

    exp_year = int(passport['eyr'])
    if not exp_year in range(2020, 2030+1):
        return False

    height = passport['hgt']
    if height.endswith('cm'):
        val = int(height[:-2])
        if not val in range(150, 193+1):
            return False
    elif height.endswith('in'):
        val = int(height[:-2])
        if not val in range(59, 76+1):
            return False
    else:
        return False

    hair_color = passport['hcl']
    if hair_color[0] != '#':
        return False
    if len(hair_color) != 7:
        return False
    for char in hair_color[1:]:
        if char not in '0123456789abcdef':
            return False

    eye_color = passport['ecl']
    eye_clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if eye_color not in eye_clrs:
        return False

    passport_id = passport['pid']
    if len(passport_id) != 9:
        return False
    for char in passport_id:
        if char not in '0123456789':
            return False

    return True


if __name__ == '__main__':
    passports = [{'dummy':None}]
    attrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # 'cid' is optional

    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                for element in line.split():
                    key, val = element.split(':')
                    passports[-1][key] = val
            else:
                # New passport
                passports.append({'dummy':None})

    complete_passports = 0
    valid_passports = 0
    for passport in passports:
        if check_complete_passport(passport, attrs):
            complete_passports += 1
        if check_valid_passport(passport, attrs):
            valid_passports += 1

    print(f'Found {complete_passports} complete passports of {len(passports)}')
    print(f'Found {valid_passports} valid passports of {complete_passports} complete passports')