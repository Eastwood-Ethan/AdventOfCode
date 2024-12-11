# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:08:10 2024
"""
from collections import deque

f = open("20241210.txt", 'r')
top_map = []
for line in f.readlines():
    top_map.append(line[:-1])
f.close()

def traverse_map(top_map, ifRating):
    # BFS
    trailheads = []
    r_len = len(top_map)
    c_len = len(top_map[0])
    
    for r in range(r_len):
        for c in range(c_len):
            if top_map[r][c] == '0':
                trailheads.append([r,c])
                
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    scores = 0

    for th in trailheads:
        visited = [th]
        score = 0
        queue = deque([th])
        while queue:
            n = len(queue)
            for i in range(n):
                loc = queue[0]
                x, y = loc[0], loc[1]
                for d in dirs:
                    dx = x + d[0]
                    dy = y + d[1]
                    if (dx in range(r_len) and dy in range(c_len) and 
                       int(top_map[dx][dy]) == int(top_map[x][y]) + 1 and 
                       ([dx, dy] not in visited or ifRating)):
                        queue.append([dx, dy])
                        visited.append([dx, dy])
                        if top_map[dx][dy] == '9':
                            score += 1
                queue.popleft()
        scores += score
        
    return scores
            
    
print("Part 1:", traverse_map(top_map, False))
print("Part 2:", traverse_map(top_map, True))