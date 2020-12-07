#!/usr/local/bin/python3

import re

rule_strings = open("07-data.txt", "r").read().split("\n")

# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
rule_pattern=re.compile("^(\w+\s+\w+)\s*bags contain ((\d.*)|(no other bags.))$")
bag_pattern=re.compile("\s*(\d+)\s*(\w+\s+\w+)\s*bag")

# parse
bags={}
for rule in rule_strings:
    res=rule_pattern.match(rule)
    outer=res.group(1)
    contained={}
    if None != res.group(3):
        for bag_str in res.group(3).split(","):
            bag_res=bag_pattern.match(bag_str)
            contained[bag_res.group(2)] = int(bag_res.group(1))
    bags[outer]=contained

# part 1
atleast={}
def atleast_rec(target, cur):
    if cur in atleast:
        return atleast[cur]
    if 0 == len(bags[cur]):
        atleast[cur] = 0
        return False
    for bag in bags[cur]:
        if target == bag:
            atleast[cur] = True
            return True
        if atleast_rec(target, bag):
            atleast[cur] = True
            return True
    return False
for bag in bags:
    atleast_rec("shiny gold", bag)

count = 0
for bag in atleast:
    if atleast[bag]:
        count += 1
print("At least {0} bags may contain a shiny gold bag".format(count))

# part 2
bagsum={}
def sum_rec(cur):
    if cur in bagsum:
        return bagsum[cur]
    if 0 == len(bags[cur]):
        bagsum[cur] = 0
        return bagsum[cur]

    csum=0
    for bag in bags[cur]:
        csum += sum_rec(bag) * bags[cur][bag] + bags[cur][bag]
    bagsum[cur] = csum
    return bagsum[cur]

for bag in bags:
    sum_rec(bag)
print("A total of {0} bags are required in a shiny gold bag".format(bagsum["shiny gold"]))