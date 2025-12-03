# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 14:16:51 2025
"""
import math

f = open("2502.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split(",")

invalidSum = 0

for interval in data:
    start, end = interval.split('-')
    if len(start) % 2 == 1:
        start = 10 ** len(start)
    if len(end) % 2 == 1:
        end = 10 ** (len(end) - 1)
    start = int(start)
    end = int(end)
    if start >= end:
        continue
    
    while start <= end:
        start = str(start)
        repeat = start[:(len(start) // 2)]
        if int(start) <= int(repeat * 2) <= end:
            invalidSum += int(repeat * 2)
        
        if len(str(int(repeat) + 1)) > len(repeat):
            repeat = str((int(repeat) + 1) * 10)
        else:
            repeat = str(int(repeat) + 1)
        start = int(repeat * 2)

print("Part 1:", invalidSum)

def divisors(n):
    divs = [x for x in range(1, int(math.sqrt(n))+1) if n % x == 0]
    return list(set(divs + [int(n/x) for x in divs]))

# Brute force :( less than 5s though
invalidSum= 0

for interval in data:
    start, end = interval.split('-')
    for i in range(int(start), int(end) + 1):
        i = str(i)
        for j in divisors(len(i)):
            if j != len(i) and i[:j] * (len(i) // j) == i:
                invalidSum += int(i)
                break
print("Part 2:", invalidSum)