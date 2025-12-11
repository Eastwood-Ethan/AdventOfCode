# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 09:30:30 2025
"""
from collections import deque, defaultdict
f = open("2511.txt", 'r')
data = f.read()
f.close()

devices = defaultdict(str)
data = data[:-1].split('\n')
for line in data:
    devices[line.split(':')[0]] = line.split(": ")[1].split(" ")
    
def numPaths(start, end):
    paths = 0
    queue = deque([start])
    loop = 0
    while queue and loop < 100000000:
        for wire in devices[queue[0]]:
            if wire == end:
                paths += 1
                loop = 0
            else:
                queue.append(wire)
                loop += 1
        queue.popleft()
    return paths
    
print("Part 1:", numPaths('you', 'out'))

# VERY UGLY answer for part 2, will definitely improve at some point 
# (runtime ~90s and no way to ensure loop count is large enough without checking if answer is correct obviously)
total = (numPaths('svr', 'fft') * numPaths('fft', 'dac') * numPaths('dac', 'out') + 
         numPaths('svr', 'dac') * numPaths('dac', 'fft') * numPaths('fft', 'out'))
print("Part 2:", total)