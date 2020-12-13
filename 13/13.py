#!/usr/local/bin/python3

import math
import numpy

timetable = "17,x,13,19".split(",")
timetable = "67,7,59,61".split(",")
timetable = "41,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,659,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,937,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17".split(",")
times=[]
for offset in range(len(timetable)):
  if timetable[offset] != "x":
    times.append([offset, int(timetable[offset])])
print(times)


cur_time = 0
step = times[0][1]

for i in range(1, len(times)):
    print(times[i])
    t_offset = times[i][0]
    t_interval = times[i][1]

    found = False
    x = 0
    while not found:
        if 0 == (cur_time + (x * step) + t_offset) % t_interval:
            found = True
            print("found", cur_time + (x * step), "offset", t_offset, "interval", t_interval)
            cur_time = cur_time + (x * step)
            step = numpy.lcm(step, t_interval)
            print("continuning with step size ", step, "from time ", cur_time)
        x += 1

print("Time: ", cur_time)