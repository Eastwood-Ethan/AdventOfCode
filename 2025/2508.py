# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 13:24:46 2025
"""
import math
from collections import defaultdict
f = open("2508.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split('\n')
for i in range(len(data)):
    data[i] = [int(x) for x in data[i].split(',')]
    
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

distances = []
for j1 in range(len(data)):
    for j2 in range(j1 + 1, len(data)):
        distances.append([distance(data[j1], data[j2]), j1, j2])
        
distances = sorted(distances)
circuits = [set([i]) for i in range(len(data))]
num_connections = 0

for path in distances:
    if num_connections == 1000:
        lengths = defaultdict(int)
        for c in circuits:
            lengths[len(c)] += 1
        biggest_circuits = 1
        for i in range(3):
            biggest_circuits *= max(lengths)
            lengths.pop(max(lengths))
        print("Part 1:", biggest_circuits)
        
    c1_loc, c2_loc = -1, -1
    for c in range(len(circuits)):
        if path[1] in circuits[c]:
            c1_loc = c
        if path[2] in circuits[c]:
            c2_loc = c
    if c1_loc != c2_loc:
        circuits[c1_loc].update(circuits[c2_loc])
        circuits.pop(c2_loc)
    num_connections += 1
    
    if len(circuits) == 1:
        print("Part 2:", data[path[1]][0] * data[path[2]][0])
        break