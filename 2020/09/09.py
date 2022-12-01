#!/usr/local/bin/python3

numbers = list(map(int, open("09-data.txt", "r").read().split("\n")))

def isvalid(nbrs, target):
    sorted=nbrs
    sorted.sort()
    x=0
    y=len(sorted)-1
    while x<y:
        sum = sorted[x] + sorted[y]
        if (sum == target):
            return True
        elif (sum < target):
            x += 1
        else:
            y -= 1
    return False

window = 25
for i in range(window + 1, len(numbers)):
    cur = numbers[i]
    if not isvalid(numbers[i-window-1:i], cur):
        print("Number {0} at position {1} is not valid".format(cur, i))


# PART 2
target=29221323
for window in range(2,30):
    # luckily, there are no numbers smaller than our target after it, so we only need to look before
    for i in range(0, 508-window):
        if target == sum(numbers[i:i+window]):
            print("found a matching sum from lines {0} to {1} with numbers {2}".format(i+1, i+window, numbers[i:i+window]))
            sorted=numbers[i:i+window]
            sorted.sort()
            min=sorted[0]
            max=sorted[len(sorted)-1]
            print("Smallest {0} and largest {1} have a sum of {2}".format(min, max, min+max))
print("done")
