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
    for i, (xi, yi) in coords.items():
        for f, (xf, yf) in coords.items():
            path = '<' * (yi - yf) + 'v' * (xf - xi) + '^' * (xi - xf) + '>' * (yf - yi)
            if scared_tile == (xi, yf) or scared_tile == (xf, yi):
                path = path[::-1]
            res[(i, f)] = path + 'A'
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

complexities_part1, complexities_part2 = 0, 0
for code in codes:
    complexities_part1 += int(code[:3]) * find_len(code, 3, True)
    complexities_part2 += int(code[:3]) * find_len(code, 26, True)

print("Part 1:", complexities_part1)
print("Part 2:", complexities_part2)
