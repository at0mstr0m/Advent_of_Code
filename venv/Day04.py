with open('Inputs\Day04input.txt', 'r') as f:
    raw_input = f.read().split('\n')

passports = [{}]
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
valid_passports1 = 0
valid_passports2 = 0

def check_required_fields(fields, required_fields):
    return all([required in fields for required in required_fields])

def check_byr(value):
    return len(value) == 4 and 1920 <= int(value) <= 2002

def check_iyr(value):
    return len(value) == 4 and 2010 <= int(value) <= 2020

def check_eyr(value):
    return len(value) == 4 and 2020 <= int(value) <= 2030

def check_hgt(value):
    unit = value[-2:]
    if unit == 'in':
        return 59 <= int(value[:-2]) <= 76
    if unit == 'cm':
        return 150 <= int(value[:-2]) <= 193
    return False

def check_hcl(value):
    return value[0] == '#' and len(value) == 7 and all(
        ['a' <= char <= 'f' or '0' <= char <= '9' for char in value[1:]])

def check_ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(value):
    return len(value) == 9 and value.isnumeric()

iterator = 0
for line in raw_input:
    if line == '':
        passports.append({})
        iterator += 1
    else:
        for data in line.split(' '):
            key, value = data.split(':')
            passports[iterator][key] = value

for passport in passports:
    fields = [data[:3] for data in passport]
    if not check_required_fields(fields, required_fields):
        continue
    valid_passports1 += 1
    if all([check_byr(passport['byr']),
            check_iyr(passport['iyr']),
            check_eyr(passport['eyr']),
            check_hgt(passport['hgt']),
            check_hcl(passport['hcl']),
            check_ecl(passport['ecl']),
            check_pid(passport['pid'])]):
        valid_passports2 += 1

print('Answer 1:', valid_passports1)
print('Answer 2:', valid_passports2)