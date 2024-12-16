# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:24:10 2024
"""
from collections import deque

f = open("16.txt", 'r')
maze = []
for line in f.readlines():
    maze.append(list(line)[:-1])
f.close()
r_len = len(maze)
c_len = len(maze[0])

def traverse_weighted_graph(maze, start_loc):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    
    scores = {}
    scores[start_loc] = 0
    
    queue = deque([(0, start_loc[0], start_loc[1], start_loc[2])])
    while queue:
        loc_score, x, y, f = queue[0]
        queue.popleft()
        if scores[(x, y, f)] >= loc_score:
            for d in range(4):
                if (x, y, d) not in scores or scores[(x, y, d)] > loc_score + 1000:
                    scores[(x, y, d)] = loc_score + 1000
                    queue.append((loc_score + 1000, x, y, d))
        
        dx = x + dirs[f][0]
        dy = y + dirs[f][1]
        if maze[dx][dy] != '#' and ((dx, dy, f) not in scores or scores[(dx, dy, f)] > loc_score + 1):
            scores[(dx, dy, f)] = loc_score + 1
            queue.append((loc_score + 1, dx, dy, f))
    return scores

scores = traverse_weighted_graph(maze, (r_len - 2, 1, 1))
min_score = float('inf')
end_dir = 0
for d in range(4):
    if (1, c_len - 2, d) in scores and min_score > scores[(1, c_len - 2, d)]:
        min_score = scores[(1, c_len - 2, d)]
        end_dir = d
        
print("Part 1:", min_score)

scores_reverse = traverse_weighted_graph(maze, (1, c_len - 2, (end_dir + 2) % 4))
seats = []
for loc in scores:
    rev_loc = (loc[0], loc[1], (loc[2] + 2) % 4)
    if rev_loc in scores_reverse and scores[loc] + scores_reverse[rev_loc] == min_score:
        seats.append((loc[0], loc[1]))
        
print("Part 2:", len(set(seats)))