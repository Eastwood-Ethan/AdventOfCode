# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:55:28 2024
"""
from collections import deque

f = open("12.txt", 'r')
garden = []
for line in f.readlines():
    garden.append(list(line[:-1]))
f.close()

r_len, c_len = len(garden), len(garden[0])
directions = [(-1,0), (0,1), (1,0), (0,-1)]
regions = []

for r in range(r_len):
    for c in range(c_len):
        if garden[r][c] != '.':
            vegetable = garden[r][c]
            region = [[r,c]]
            queue = deque([[r,c]])
            garden[r][c] = '.'
            while queue:
                for _ in range(len(queue)):
                    x, y = queue[0][0], queue[0][1]
                    for d in directions:
                        dx = x + d[0]
                        dy = y + d[1]
                        if dx in range(r_len) and dy in range(c_len) and garden[dx][dy] == vegetable:
                            queue.append([dx, dy])
                            region.append([dx, dy])
                            garden[dx][dy] = '.'
                    
                    queue.popleft()
                    
            regions.append(region)
        
perimiters = []
for region in regions:
    p = 0
    for loc in region:
        x, y = loc[0], loc[1]
        for d in directions:
            dx = x + d[0]
            dy = y + d[1]
            if [dx, dy] not in region:
                p += 1
    perimiters.append(p)
    
areas = []
for region in regions:
    areas.append(len(region))
    
price = 0
for i in range(len(areas)):
    price += perimiters[i] * areas[i]
    
print("Part 1:", price)


# list copying not working, not sure why
f = open("12.txt", 'r')
garden = []
for line in f.readlines():
    garden.append(list(line[:-1]))
f.close()
# Number of edges is the same as the number of corners
corners = []
for region in regions:
    v = garden[region[0][0]][region[0][1]]
    corner = 0
    for cell in region:
        local = [[0] * 3, [0, 1, 0], [0] * 3]
        for i in range(-1, 2):
            for j in range(-1, 2):
                if cell[0] + i in range(r_len) and cell[1] + j in range(c_len): 
                    local[i + 1][j + 1] = garden[cell[0] + i][cell[1] + j] == v
        
        # Concave and convex corners
        corner += (((not local[0][0]) and (local[0][1] == local[1][0])) +
                    ((not local[0][2]) and (local[0][1] == local[1][2])) +
                    ((not local[2][0]) and (local[2][1] == local[1][0])) +
                    ((not local[2][2]) and (local[2][1] == local[1][2])))
        # Cells only connected via the diagonal
        corner += ((local[0][0] and not local[0][1] and not local[1][0]) +
                   (local[0][2] and not local[0][1] and not local[1][2]) +
                   (local[2][0] and not local[2][1] and not local[1][0]) +
                   (local[2][2] and not local[2][1] and not local[1][2]))
        
    corners.append(corner)
    
price = 0
for i in range(len(corners)):
    price += corners[i] * areas[i]
    
print("Part 2:", price)
        
