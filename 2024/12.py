# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 14:55:28 2024

@author: ethan.eastwood
"""
from collections import deque

f = open("12.txt", 'r')
garden = []
for line in f.readlines():
    garden.append(list(line[:-1]))
f.close()

f = '''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE'''
garden = []
for line in f.split('\n'):
    garden.append(list(line))
    
gc = garden[:]


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

# region[0] is always on the edge and we can start on the top edge
# traverse along the edge clockwise
# every time we hit a corner, add one to the side list and change direction
# don't update the current pos when hitting a convex corner, you want to start the next side at the same pos
# update current pos when hitting concave corner
# because of this we will only count a side when we have finished traversing it
# end loop when we are back at original pos and facing the same direction as when we started

# Actually this won't work in case of "lakes"

# edges_list = []
# for region in regions:
#     start = region[0]
#     facing = 1
#     edges = 0
#     started = False
#     pos = start
#     print(regions.index(region))
#     while not started or not (pos == start and facing == 1):
#         started = True
#         # up is d-1 and down is d+1
#         forward_straight = [pos[0] + directions[facing][0], pos[1] + directions[facing][1]]
#         forward_up = [pos[0] + directions[facing][0] + directions[(facing - 1) % 4][0], 
#                       pos[1] + directions[facing][1] + directions[(facing - 1) % 4][1]]
        
#         if forward_up in region: #left (concave) turn
#             pos = forward_up
#             facing = (facing + 1) % 4
#             edges += 1
#             #print("left turn")
            
#         elif forward_straight in region: # move straight
#             pos = forward_straight
#             #print("straight")
            
#         else: #right (convex) turn
#             facing = (facing + 1) % 4
#             edges += 1
#             #print("right turn")
            
#         print(start, pos, facing, not started or not (pos == start and facing == 1))
#     print('\n')
#     edges_list.append(edges)
    
# print(edges_list)