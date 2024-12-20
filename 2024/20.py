# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:56:41 2024
"""
from collections import deque, defaultdict
f = open('20.txt', 'r')
data = f.read().splitlines()
f.close()
start, end, maze = 0, 0, {}
r_len, c_len = len(data), len(data[0])

# Find the start and end locations, put the maze locations into a dictionary
for i in range(r_len):
    data[i] = list(data[i])
    if 'S' in data[i]:
        start = i + data[i].index('S') * 1j
    if 'E' in data[i]:
        end  =  i + data[i].index('E') * 1j
        
    for j in range(c_len):
        maze[i + j*1j] = data[i][j]
        
    
# Create the list of nodes you can get in 2 ps
dirs = [-1, 1j, 1, -1j]
two_dirs = {}
for i in dirs:
    for j in dirs:
        if i + j != 0 and i + j not in two_dirs:
            two_dirs[i + j] = 2
            
# Create the list of nodes you can get in 20 ps          
twenty_dirs = {0:0}
cheat_length = 1
while cheat_length <= 20:
    next_dict = {}
    for loc in twenty_dirs:
        for d in dirs:
            if loc + d not in twenty_dirs:
                next_dict[loc + d] = cheat_length
    twenty_dirs.update(next_dict)
    cheat_length += 1
        
# Return a weighted list of nodes where n=how far from start you are
def bfs(maze, start):
    dirs = [-1, 1j, 1, -1j]
    visited = {}
    q = deque([start])
    n = 0
    
    while q:
        len_q = len(q)
        
        for i in range(len_q):
            loc = q[0]
            q.popleft()
            visited[loc] = n
            
            for d in dirs:
                new_loc = loc + d
                if new_loc not in visited and maze[new_loc] != '#':
                    q.append(new_loc)
        n += 1
        
    return visited

# Loop through maze locations and then through possible cheats to see if it is faster to use the cheat
def num_saved(maze, dirs, maze_from_start, maze_from_end):
    time_saved = defaultdict(int)
    for loc in maze:
        if maze[loc] != '#':
            for d in dirs:
                new_loc = loc + d
                if new_loc in maze and maze[new_loc] != '#':
                    if maze_from_start[new_loc] > maze_from_start[loc]:
                        saved = maze_from_start[end] - (maze_from_start[loc] + maze_from_end[new_loc]) - dirs[d]
                        time_saved[saved] += 1
    saved = 0
    for t in time_saved:
        if t > 99:
            saved += time_saved[t]
    return saved

# Get the weighted graph from the start of the race and the end
maze_from_start = bfs(maze, start)
maze_from_end = bfs(maze, end)

print("Part 1:", num_saved(maze, two_dirs, maze_from_start, maze_from_end))
print("Part 2:", num_saved(maze, twenty_dirs, maze_from_start, maze_from_end))
