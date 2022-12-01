#!/usr/local/bin/python3

import re

file = open("02-data.txt", "r")

passwords=file.read().split("\n")


# Part 1
valid=0
invalid=0
pattern=re.compile('(\d+)-(\d+)\s(\w):\s*(\w+)')
for password in passwords:
    match = pattern.match(password)

    min=int(match.group(1))
    max=int(match.group(2))
    letter=match.group(3)
    password=match.group(4)

    occurences=password.count(letter)
    if (occurences >= min and occurences <= max):
        valid=1+valid
    else:
        invalid=1+invalid

print("Part 1) Valid: {0} Invalid: {1}".format(valid, invalid))

# Part 2
valid=0
invalid=0
pattern=re.compile('(\d+)-(\d+)\s(\w):\s*(\w+)')
for password in passwords:
    match = pattern.match(password)

    min=int(match.group(1))
    max=int(match.group(2))
    letter=match.group(3)
    password=match.group(4)

    if ((password[min-1] == letter) ^ (password[max-1] == letter)):
        valid=1+valid
    else:
        invalid=1+invalid

print("Part 2) Valid: {0} Invalid: {1}".format(valid, invalid))