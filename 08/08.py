#!/usr/local/bin/python3

import re

instructions = open("08-data.txt", "r").read().split("\n")

pattern=re.compile("(acc|jmp|nop) ([+-]\d+)")

def run_program(code):
    visited={}
    pos = 0
    acc = 0
    while (pos < len(code)):
        # part 1: infinite loop detection
        if pos in visited:
            return "Been here before in line {0}. Current acc value is {1}".format(pos, acc)
        visited[pos] = True

        res=pattern.match(code[pos])
        op = res.group(1)
        val = int(res.group(2))
        if "acc" == op:
            acc += val
            pos += 1
        elif "jmp" == op:
            pos += val
        elif "nop" == op:
            pos += 1
        else:
            raise Exception("Unknown operation {0}".format(code[pos]))
    return acc

print(run_program(instructions))
    


# part 2
for changed_pos in range(0, len(instructions)):
    new_instructions = instructions.copy()
    res=pattern.match(new_instructions[changed_pos])
    op = res.group(1)
    val = res.group(2)
    if "acc" == op:
        continue

    # change instruction
    if "jmp" == op:
        new_instructions[changed_pos] = "nop {0}".format(val)
    elif "nop" == op:
        new_instructions[changed_pos] = "jmp {0}".format(val)
    # try running it
    res = run_program(new_instructions)
    if isinstance(res, int):
        print("Changing the instructions at line {0} made the program terminate with acc {1}".format(changed_pos, res))
        break
print("done")
    
