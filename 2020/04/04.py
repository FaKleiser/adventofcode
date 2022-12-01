#!/usr/local/bin/python3

import re

file = open("04-data-normalized.txt", "r")

passports=file.read().split("\n")

kvpattern = re.compile('(\w{3}):([\w#]+)')
hgtpattern = re.compile('^(\d+)(cm|in)$')
hexpattern = re.compile('^#[a-f0-9]{6}$')
eyepattern = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pidpattern = re.compile('^(\d{9})$')

def isvalid(passport):
    required=['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required:
        if not (key in passport):
            return False
    return True

def isvalid_parttwo(passport):
    for key in passport:
        value = passport[key]
        if 'byr' == key:
            byr=int(value)
            if byr < 1920 or byr > 2002:
                return False
        elif 'iyr' == key:
            iyr=int(value)
            if iyr < 2010 or iyr > 2020:
                return False
        elif 'eyr' == key:
            eyr=int(value)
            if eyr < 2020 or eyr > 2030:
                return False
        elif 'hgt' == key:
            hgt=hgtpattern.match(value)
            if None == hgt:
                return False
            height=int(hgt.group(1))
            if hgt.group(2) == 'in':
                if height < 59 or height > 76:
                    return False
            else:
                if height < 150 or height > 193:
                    return False
        elif 'hcl' == key:
            if None == hexpattern.match(value):
                return False
        elif 'ecl' == key:
            if None == eyepattern.match(value):
                return False
        elif 'pid' == key:
            if None == pidpattern.match(value):
                return False
    return True

valid = 0
validPartTwo=0
for passportStr in passports:
    # print(passportStr)
    match = kvpattern.findall(passportStr)
    passport={}
    for item in match:
        passport[item[0]] = item[1]
    if isvalid(passport):
        valid += 1
        if isvalid_parttwo(passport):
            validPartTwo += 1
print("Part 1: There are {0} valid passports".format(valid))
print("Part 2: There are {0} valid passports".format(validPartTwo))

