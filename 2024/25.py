# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:10:38 2024
"""

f = open('25.txt', 'r')
data = f.read().split('\n\n')
f.close()
keys = []
locks = []
for i in range(len(data)):
    data[i] = data[i].splitlines()
    isLock = data[i][0] == '#####'
    data[i] = [s.count('#') for s in [''.join(s) for s in zip(*data[i])]]
    if isLock:
        locks.append(data[i])
    else:
        keys.append(data[i])

num_fit = 0
for k in keys:
    for l in locks:
        fits = True
        for i in [i[0] + i[1] for i in zip(k, l)]:
            if i > 7:
                fits = False
                break
        num_fit += fits
        
print("Part 1:", num_fit)
