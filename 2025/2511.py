# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 09:30:30 2025
"""
from collections import defaultdict
f = open("2511.txt", 'r')
data = f.read()
f.close()

devices = defaultdict(str)
data = data[:-1].split('\n')
for line in data:
    devices[line.split(':')[0]] = line.split(": ")[1].split(" ")

memo = {}
def numPaths(start, end):
    if (start, end) in memo:
        return memo[(start, end)]
    
    if start == end:
        return 1
    else:
        memo[(start, end)] = sum(numPaths(next_device, end) for next_device in devices[start])
        
    return memo[(start, end)]
    
print("Part 1:", numPaths('you', 'out'))

total = (numPaths('svr', 'fft') * numPaths('fft', 'dac') * numPaths('dac', 'out') + 
          numPaths('svr', 'dac') * numPaths('dac', 'fft') * numPaths('fft', 'out'))

print("Part 2:", total)
