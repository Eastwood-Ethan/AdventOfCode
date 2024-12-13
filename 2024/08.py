# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:58:54 2024
"""
from collections import defaultdict

f = open("08.txt", 'r')
ant_map = []
for line in f.readlines():
    ant_map.append(line[:-1])
f.close()

def check_antinodes(ant_map, p1, p2, antinodes):
    if 0 <= p1[0] < len(ant_map) and 0 <= p1[1] < len(ant_map[0]) and p1 not in antinodes:
        antinodes.append(p1)
    if 0 <= p2[0] < len(ant_map) and 0 <= p2[1] < len(ant_map[0]) and p2 not in antinodes:
        antinodes.append(p2)
    return antinodes

def find_antinodes(ant_map, part2):
    ant_loc = defaultdict(list)
    r_len = len(ant_map)
    c_len = len(ant_map[0])

    for i in range(r_len):
        for j in range(c_len):
            if ant_map[i][j] != '.':
                ant_loc[ant_map[i][j]].append([i, j])
                
    antinodes = []

    for f in ant_loc:
        for i in ant_loc[f]:
            for j in ant_loc[f]:
                if i != j:
                    m = [i[0] - j[0], i[1] - j[1]]
                    
                    if not part2:
                        p1 = [i[0] + m[0], i[1] + m[1]]
                        p2 = [j[0] - m[0], j[1] - m[1]]
                        antinodes = check_antinodes(ant_map, p1, p2, antinodes)
                    
                    else:
                        k = 0
                        while ((i[0] + k * m[0] in range(r_len) and i[1] + k * m[1] in range(c_len)) or 
                              (j[0] - k * m[0] in range(r_len) and j[1] - k * m[1] in range(c_len))):
                            
                            p1 = [i[0] + k * m[0], i[1] + k * m[1]]
                            p2 = [j[0] - k * m[0], j[1] - k * m[1]]
                            
                            antinodes = check_antinodes(ant_map, p1, p2, antinodes)
                                
                            k += 1
                        
    return len(antinodes)

print("Part 1:", find_antinodes(ant_map, False))
print("Part 2:", find_antinodes(ant_map, True))

