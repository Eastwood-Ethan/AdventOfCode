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

outline = []
for i in range(-1, 71):
    outline.append(i + -1j)
    outline.append(i + 71 * 1j)
    outline.append(i * 1j - 1)
    outline.append(i * 1j + 71)
outline.append(71 + 71*1j)

def bfs(corrupted_spaces, cur_loc = 0):
    dirs = [-1, 1j, 1, -1j]
    q = deque([cur_loc])
    visited = [cur_loc] + corrupted_spaces
    steps = 0
    while q:
        l = len(q)
        for i in range(l):
            cur_loc = q[0]
            q.popleft()
            for d in dirs:
                if cur_loc + d not in visited:
                    q.append(cur_loc + d)
                    visited.append(cur_loc + d)
        steps += 1
        if 70 + 70 * 1j in visited:
            break
        
    return 70 + 70 * 1j in visited, steps
    
print("Part 1:", bfs(bytelist[:1024] + outline)[1])

low = 1024
high = len(bytelist) - 1
mid = (high + low) // 2

while low + 1 < high:
    if bfs(outline + bytelist[:mid])[0]:
        low = mid
    else:
        high = mid
    mid = (high + low) // 2
print("Part 2:", str(int(bytelist[low].real)) + ',' + str(int(bytelist[low].imag)))
