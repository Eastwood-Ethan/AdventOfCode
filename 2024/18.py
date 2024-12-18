# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:21:17 2024
"""
from collections import deque
f = open('18.txt', 'r')
bytelist = f.read().splitlines()
for i in range(len(bytelist)):
    bytelist[i] = list(map(int, bytelist[i].split(',')))
    bytelist[i] = bytelist[i][0] + bytelist[i][1] * 1j
f.close()

corrupted_spaces = bytelist[:1024]

for i in range(-1, 71):
    corrupted_spaces.append(i + -1j)
    corrupted_spaces.append(i + 71 * 1j)
    corrupted_spaces.append(i * 1j - 1)
    corrupted_spaces.append(i * 1j + 71)
corrupted_spaces.append(71 + 71*1j)

def bfs(corrupted_spaces, cur_loc):
    dirs = [-1, 1j, 1, -1j]
    q = deque([cur_loc])
    visited = [cur_loc]
    steps = 0
    while q:
        l = len(q)
        for i in range(l):
            cur_loc = q[0]
            q.popleft()
            for d in dirs:
                if cur_loc + d not in visited and cur_loc + d not in corrupted_spaces:
                    q.append(cur_loc + d)
                    visited.append(cur_loc + d)
        steps += 1
        if 70 + 70 * 1j in visited:
            break
        
    return 70 + 70 * 1j in visited, steps
    
print("Part 1:", bfs(corrupted_spaces, 0)[1])

i = 1024
while bfs(corrupted_spaces, 0)[0]:
    corrupted_spaces.append(bytelist[i])
    i += 1
    print(i)
print("Part 2:", corrupted_spaces[-1])
    