#!/usr/local/bin/python3


file_contents = open("06-data.txt", "r").read()

def parseGroup(groupStr):
    group={}
    group['answers']=groupStr.split("\n")
    return group
groups=list(map(parseGroup, file_contents.split("\n\n")))

# part1
sum_of_counts=0
for group in groups:
    set_of_answers=set()
    for answer in group['answers']:
        set_of_answers.update({char for char in answer})
    sum_of_counts+=len(set_of_answers)
print("The sum of the counts to which ANYONE answered yes is {0}".format(sum_of_counts))

# part1
sum_of_counts=0
for group in groups:
    all_set={char for char in group['answers'][0]}
    for answer in group['answers']:
        answer_set={char for char in answer}
        all_set = all_set.intersection(answer_set)
    sum_of_counts+=len(all_set)
print("The sum of the counts to which EVERYONE answered yes is {0}".format(sum_of_counts))
