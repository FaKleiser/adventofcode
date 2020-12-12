#!/usr/local/bin/python3

import re

instructions = open("12-data.txt", "r").read().split("\n")

east=0
south=0
# north = 0, east = 1, south = 2, west =3
direction=1

# part 1
for instruction in instructions:
    cmd=instruction[0]
    val=int(instruction[1:])

    if "L" == cmd:
        direction = (direction - val/360*4)%4
    elif "R" == cmd:
        direction = (direction + val/360*4)%4
    elif "F" == cmd:
        if 1 == direction or 3 == direction:
            east -= (direction-2)*val
        else:
            south += (direction-1)*val
    elif "N" == cmd:
        south -= val
    elif "S" == cmd:
        south += val
    elif "E" == cmd:
        east += val
    elif "W" == cmd:
        east -= val
print("Reached east {0} and south {1} with manhattan distance {2}".format(east, south, east+south))

east=0
south=0
# north = 0, east = 1, south = 2, west =3
direction=1
wp_east=10
wp_south=-1

# part 2
for instruction in instructions:
    cmd=instruction[0]
    val=int(instruction[1:])

    if "L" == cmd:
        if val == 180 or val == 270:
            wp_east *= -1
            wp_south *= -1
        if val == 90 or val == 270:
            tmp = wp_east
            wp_east = wp_south
            wp_south = tmp * -1
    elif "R" == cmd:
        if val == 180 or val == 270:
            wp_east *= -1
            wp_south *= -1
        if val == 90 or val == 270:
            tmp = wp_south
            wp_south = wp_east
            wp_east = tmp * -1
    elif "F" == cmd:
        east += wp_east*val
        south += wp_south*val
    elif "N" == cmd:
        wp_south -= val
    elif "S" == cmd:
        wp_south += val
    elif "E" == cmd:
        wp_east += val
    elif "W" == cmd:
        wp_east -= val
print("Reached east {0} and south {1} with manhattan distance {2}".format(east, south, east+south))