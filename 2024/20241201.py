# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 12:51:15 2024
"""

from collections import defaultdict

f = open("20241201.txt", 'r')
data = f.read()
f.close()

data = data.split("\n")[:-1]
for i in range(len(data)):
    data[i] = data[i].split('   ')
    
data = list(zip(*data[::-1]))
for i in range(2):
    data[i] = sorted(data[i])
    
distance = 0
for i in range(len(data[0])):
    distance += abs(int(data[0][i]) - int(data[1][i]))
    
print("Part 1:", str(distance))

hashmap = defaultdict(int)
for n in data[1]:
    hashmap[int(n)] += 1
similarity = 0
for n in data[0]:
    similarity += int(n) * hashmap[int(n)]
    
print("Part 2:", str(similarity))
