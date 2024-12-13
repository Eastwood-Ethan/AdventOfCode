# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:37:44 2024
"""

f = open("06.txt", 'r')
guard_map = []
for line in f.readlines():
    guard_map.append(list(line)[:-1])
f.close()

r_len = len(guard_map)
c_len = len(guard_map[0])
guard_loc = ()

for r in range(r_len):
    if not guard_loc:
        for c in range(c_len):
            if guard_map[r][c] == '^':
                guard_loc = (r,c)
                break
d = [(-1,0), (0,1), (1,0), (0,-1)]
facing = 0
loop = 0

def sim_guard(guard_loc, facing, visited):
    temp_visited = visited[:]
    while 0 <= guard_loc[0] < r_len and 0 <= guard_loc[1] < c_len:
        if (guard_loc[0], guard_loc[1], facing) in temp_visited:
            return 'loop'
        temp_visited.append((guard_loc[0], guard_loc[1], facing))
        
        dx = guard_loc[0] + d[facing][0]
        dy = guard_loc[1] + d[facing][1]
        if 0 > dx or dx >= r_len or 0 > dy or dy >= c_len:
            break
        
        while guard_map[dx][dy] == '#':
            facing = (facing + 1) % 4
            dx = guard_loc[0] + d[facing][0]
            dy = guard_loc[1] + d[facing][1]
            
            if 0 > dx or dx >= r_len or 0 > dy or dy >= c_len:
                break
        else:
            guard_loc = (dx,dy)
            
    return temp_visited

visited = sim_guard(guard_loc, facing, [])
visited_part1 = []
for e in visited:
    if (e[0], e[1]) not in visited_part1:
        visited_part1.append((e[0], e[1]))
print("Part 1:", len(visited_part1))
