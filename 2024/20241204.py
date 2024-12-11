# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:00:40 2024
"""

f = open("20241204.txt", 'r')
data = f.readlines()
f.close()

r_len, c_len = len(data), len(data[0])
xmas_count = 0

for r in range(r_len):
    for c in range(c_len):
        if data[r][c] == 'X':
            
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    
                    if ((i != 0 or j != 0) and
                       ((i == -1 and r >= 3) or i == 0 or (i == 1 and r < r_len - 3)) and
                       ((j == -1 and c >= 3) or j == 0 or (j == 1 and c < c_len - 3)) and
                       (data[r + i][c + j] + data[r + 2*i][c + 2*j] + data[r + 3*i][c + 3*j] == 'MAS')):
                        xmas_count += 1
print("Part 1:", xmas_count)

x_mas_count = 0
for r in range(1, r_len-1):
    for c in range(1, c_len-1):
        if data[r][c] == 'A' and (data[r-1][c-1] + data[r+1][c+1] in ['MS', 'SM']) and (data[r-1][c+1] + data[r+1][c-1] in ['MS', 'SM']):
                x_mas_count += 1
print("Part 2:", x_mas_count)