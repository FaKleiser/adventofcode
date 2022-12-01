#!/usr/local/bin/python3

numbers = list(map(int, open("10-data.txt", "r").read().split("\n")))

# part 1
sorted=numbers
sorted.append(0) # the adapter in the plane
sorted.append(max(numbers)+3) # the device
sorted.sort()
differences={}
for i in range(1, len(sorted)):
    difference=sorted[i]-sorted[i-1]
    if difference in differences:
        differences[difference] += 1
    else:
        differences[difference] = 1
print(differences)


# part 2
choices={}
choices[len(numbers)-1] = 0 # at device we're done and have no choice
def compute_choices(idx):
    if idx in choices:
        return choices[idx]
    next = 1+idx
    cur_choices = -1
    while next < len(numbers) and sorted[next] - sorted[idx] <= 3:
        cur_choices += 1 + compute_choices(next)
        next += 1
    choices[idx] = cur_choices
    return cur_choices
compute_choices(0)
print(choices[0]+1) # we need to add 1 because the first choice is never counted in the recursion because of the -1