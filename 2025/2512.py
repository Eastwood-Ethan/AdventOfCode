# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 08:42:40 2025
"""
import numpy as np
f = open("2512.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split("\n\n")
regions = [[list(map(int, r.split(': ')[0].split('x'))), list(map(int, r.split(': ')[1].split(' ')))] for r in data[-1].split("\n")]
shapes = [s.split("\n")[1:] for s in data[:-1]]
shape_areas = [sum(r.count('#') for r in s) for s in shapes]

too_small, big_enough, difficult_packing_problem = 0, 0, 0
for r, s in regions:
    if r[0] * r[1] < np.dot(s, shape_areas):
        too_small += 1
    elif r[0] * r[1] >= sum(s) * 9:
        big_enough += 1
    else:
        difficult_packing_problem += 1
# Simple sanity check reveals this problem is a troll, this feels dirty though. Perhaps generalize in the future
if not difficult_packing_problem: print("Part 1:", big_enough)
else: print("Part 1: At least", big_enough, "and at most", big_enough + difficult_packing_problem)