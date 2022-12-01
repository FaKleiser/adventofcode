#!/usr/local/bin/python3

def play(starting, turns):
    mem = {}
    def memorize(number, turn):
        if number in mem:
            mem[number].append(turn)
        else:
            mem[number] = [turn]

    spoken = None
    for turn in range(1, turns+1):
        if turn <= len(starting):
            # starting sequence
            spoken = starting[turn-1]
            memorize(spoken, turn)
        elif spoken in mem and len(mem[spoken]) == 1:
            spoken = 0
            memorize(spoken, turn)
        else:
            spoken = mem[spoken][-1] - mem[spoken][-2]
            memorize(spoken, turn)
        if turn % 250000 == 0:
            print("Turn {0}: spoke number {1}".format(turn, spoken))

    print("At the end of turn {0} the last number spoken was {1} with starting {2}".format(turns, spoken, starting))

play([0,3,6], 10)
play([1,3,2], 2020)
play([19,20,14,0,9,1], 2020)

# part 2
play([19,20,14,0,9,1], 30000000)