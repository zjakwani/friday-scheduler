
import os
import sys
from heapq import *

settings = {}
with open(os.path.join(sys.path[0], "jummah_settings.txt"), "r") as f:
    for line in f:
        name, times = line.split(":")
        times = [int(x.strip()) - 1 for x in times.split(",")]
        settings[name] = times
# Zain Jakwani 02/04/22
recordfile = open(os.path.join(sys.path[0], "jummah_records.txt"), "r")
records = recordfile.readlines()
mru = []
for _line in reversed(records):
    line2 = _line.split(":")
    line3 = line2[1] if len(line2) > 1 else line2[0]
    line = line3.replace("|", ",")
    week_names = list(set([x.strip() for x in line.split(",")]))
    for name in week_names:
        if name not in mru:
            mru.append(name)

capacity = [3,3,1]
res = [[],[],[]]
cur = ["", [-1]]
while len(res[0]) < capacity[0] or len(res[1]) < capacity[1] or len(res[2]) < capacity[2]:
    if len(cur[1]) == 1:
        popped = mru.pop()
        cur = [popped, settings[popped]]
    name, available = cur
    if len(res[0]) < capacity[0] and 0 in available:
        res[0].append(name)
        cur[1].remove(0)
    elif len(res[1]) < capacity[1] and 1 in available:
        res[1].append(name)
        cur[1].remove(1)
    elif len(res[2]) < capacity[2] and 2 in available:
        res[2].append(name)
        cur[1].remove(2)
    else:
        popped = mru.pop()
        cur = [popped, settings[popped]]

print("Copy paste into records:")
print("(Put date here):" + "|".join([(",").join(x) for x in res]) + "\n")
print("This week's schedule")
print("1st Jummah: " + ", ".join(res[0]))
print("2nd Jummah: " + ", ".join(res[1]))
print("3rd Jummah: " + ", ".join(res[2]))
