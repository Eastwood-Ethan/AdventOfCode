# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 12:49:00 2025
"""

f = open("2507.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split('\n')
for i in range(len(data)):
    data[i] = list(data[i])
    for j in range(len(data[i])):
        if data[i][j] == '.':
            data[i][j] = 0

splits = 0
for r in range(1, len(data)):
    for c in range(len(data[0])):
        if data[r-1][c] == 'S':
            data[r][c] = 1
        elif data[r][c] == '^':
            data[r][c-1] += data[r-1][c]
            data[r][c+1] += data[r-1][c]
            if data[r-1][c] != 0:
                splits += 1
        else:
            if data[r-1][c] != '^':
                data[r][c] += data[r-1][c]
                
print("Part 1:", splits)
print("Part 2:", sum(data[-1]))