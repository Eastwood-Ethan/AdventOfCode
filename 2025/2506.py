# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 12:04:36 2025
"""
import math

f = open("2506.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split('\n')
for i in range(len(data)):
    data[i] = data[i].split()

operations = data.pop()
data = list(map(list, zip(*[(int(x) for x in data[i]) for i in range(len(data))])))

total = 0
for i in range(len(data)):
    if operations[i] == '+':
        total += sum(data[i])
    else:
        total += math.prod(data[i])
        
print("Part 1:", total)



f = open("2506.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split('\n')
operations = data.pop().split()

for i in range(len(data)):
    data[i] = list(data[i])
data = list(map(list, zip(*data)))

data = ["".join(data[i]).split() for i in range(len(data))]

operation = 0
total = 0
subtotal = 0
if operations[0] == '*':
    subtotal = 1
for i in range(len(data)):
    if data[i] == []:
        total += subtotal
        subtotal = 0
        operation += 1
        if operations[operation] == '*':
            subtotal = 1
        continue
    else:
        data[i] = data[i][0]
            
    if operations[operation] == '+':
        subtotal += int(data[i])
    else:
        subtotal *= int(data[i])
        
total += subtotal
print("Part 2:", total)