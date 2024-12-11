# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:05:08 2024
"""

f = open("20241202.txt", 'r')
data = []
for line in f.readlines():
    data.append([int(num) for num in line.split(' ')])
f.close()

def safeReport(r):
    if r[0] - r[1] == 0:
        return 0
    elif r[1] - r[0] > 0:
        inc = [1, 2, 3]
    else:
        inc = [-1, -2, -3]
    
    for i in range(1, len(r)):
        if r[i] - r[i-1] not in inc:
            return 0
    return 1

safe_reports = 0
for r in data:
    safe_reports += safeReport(r)
print("Part 1:", safe_reports)

safe_reports = 0
for r in data:
    if safeReport(r):
        safe_reports += 1
    else:
        for i in range(len(data)):
            if safeReport(r[:i] + r[i+1:]):
                safe_reports += 1
                break
print("Part 2:", safe_reports)