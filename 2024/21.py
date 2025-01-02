# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 13:50:30 2024
"""
from functools import cache
f = open('21.txt', 'r')
codes = f.read().splitlines()
f.close()

def path_memo(coords, scared_tile):
    res = {}
    for i in coords.items():
        for f in coords.items():
            path = '<' * (i[1][1] - f[1][1]) + 'v' * (f[1][0] - i[1][0]) + '^' * (i[1][0] - f[1][0]) + '>' * (f[1][1] - i[1][1])
            if scared_tile == (i[1][0], f[1][1]) or scared_tile == (f[1][0], i[1][1]):
                path = path[::-1]
            res[(i[0], f[0])] = path + 'A'
    return res

numpad_coords = {c: (y, x) for y, row in enumerate(["789", "456", "123", " 0A"]) for x, c in enumerate(row)}
arrow_coords = {c: (y, x) for y, row in enumerate([" ^A", "<v>"]) for x, c in enumerate(row)}
      
numpad_memo = path_memo(numpad_coords, (3,0))
arrow_memo = path_memo(arrow_coords, (0,0))

@cache
def find_len(code, num_robots, numpad=False):
    memo = numpad_memo if numpad else arrow_memo
    if num_robots == 0:
        return len(code)
    robot_pos = 'A'
    length = 0
    
    for c in code:
        length += find_len(memo[(robot_pos, c)], num_robots - 1)
        robot_pos = c
    return length

complexities = 0
for code in codes:
    complexities += int(code[:3]) * find_len(code, 3, True)

print("Part 1:", complexities)

complexities = 0
for code in codes:
    complexities += int(code[:3]) * find_len(code, 26, True)

print("Part 2:", complexities)
