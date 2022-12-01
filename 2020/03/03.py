#!/usr/local/bin/python3

file = open("03-data.txt", "r")

treemap=list(map(list, file.read().split("\n")))


def trees(stepX, stepY):
    trees=0
    spaces=0

    x = 0
    for y in range(0,len(treemap)):
        if 0 != (y % stepY):
            continue
        if treemap[y][x] == "#":
            trees += 1
        else:
            spaces += 1
        # print("At ({0},{1}) with {2}".format(x,y,treemap[y][x]))
        x=(x+stepX) % (len(treemap[0]))

    print("Right {0}, down {1}: found {2} trees and {3} spaces".format(stepX, stepY, trees, spaces))


trees(1, 1)
trees(3, 1)
trees(5, 1)
trees(7, 1)
trees(1, 2)