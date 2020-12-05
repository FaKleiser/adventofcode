#!/usr/local/bin/python3

import re


def parseSeat(seatStr):
    seatStr = seatStr.replace('F', '0').replace('B', '1')
    seatStr = seatStr.replace('L', '0').replace('R', '1')
    seat = {}
    seat['row'] = int(seatStr[0:7], 2)
    seat['col'] = int(seatStr[7:10], 2)
    seat['id'] = seat['row']*8+seat['col']
    return seat



file = open("05-data.txt", "r")

seats=list(map(parseSeat, file.read().split("\n")))

# part 1
ids = list(map(lambda seat: seat['id'], seats))
print("Maximum seat id found is {0}", max(ids))
    

# part 2
ids.sort()
for x in range(0, len(ids)-1):
    if ids[x]+2 == ids[x+1]:
        seatid=ids[x]+1
        col=seatid%8
        row=(seatid-col)/8
        print("Our seat number is row {0} col {1} with id {seatid}", row, col, seatid)