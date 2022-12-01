#!/usr/local/bin/python3

import math
import numpy
import re
import sys


lines = open("14-data.txt", "r").read().split("\n")

def parse_mask(mask):
    rmask = mask[::-1]
    maskZeros = sys.maxsize
    maskOnes = 0
    for pos in range(0,len(mask)):
        if "1" == rmask[pos]:
            maskOnes |= 1 << pos
        if "0" == rmask[pos]:
            maskZeros ^= 1 << pos
    return maskZeros, maskOnes

def apply_mask(mask, val):
    maskZeros = mask[0]
    maskOnes = mask[1]
    val &= maskZeros
    val |= maskOnes
    return val


pattern_mask = re.compile("mask = ([01X]+)")
pattern_mem = re.compile("mem\[(\d+)\] = (\d+)")

# part 1
mask = None
mem = {}
for line in lines:
    res_mask = pattern_mask.match(line)
    res_mem = pattern_mem.match(line)
    if None != res_mask:
        mask = parse_mask(res_mask.group(1))
    elif None != res_mem:
        adr = int(res_mem.group(1))
        val = int(res_mem.group(2))
        mem[adr] = apply_mask(mask, val)

sum = 0
for key in mem:
    sum += mem[key]
print("Part 1: Sum of all numbers in memory is ", sum)

# part 2
def expand_floating_mask(mask):
    masks = [mask]
    for pos in range(0,len(mask)):
        if mask[pos] == "X":
            newmasks = []
            for m in masks:
                a = list(m)
                a[pos] = "0"
                newmasks.append("".join(a))
                a[pos] = "1"
                newmasks.append("".join(a))
            masks = newmasks
        else:
            for i in range(len(masks)):
                masks[i] = masks[i][:pos] + "X" + masks[i][pos+1:]
    return list(map(parse_mask, masks))

mask = None
floating_masks = []
mem = {}
for line in lines:
    res_mask = pattern_mask.match(line)
    res_mem = pattern_mem.match(line)
    if None != res_mask:
        mask = parse_mask(res_mask.group(1))
        floating_masks = expand_floating_mask(res_mask.group(1))
    elif None != res_mem:
        val = int(res_mem.group(2))
        adr = int(res_mem.group(1))
        adr |= mask[1]
        for fmask in floating_masks:
            fadr = adr
            fadr = apply_mask(fmask, fadr)
            mem[fadr] = val

sum = 0
for key in mem:
    sum += mem[key]
print("Part 2: Sum of all numbers in memory is ", sum)