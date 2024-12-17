# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:13:09 2024
"""
import matplotlib.pyplot as plt

f = open("14.txt", 'r')
robots = []
for line in f.readlines():
    robots.append(line[:-1].split(" "))
    robots[-1][0] = list(map(int, robots[-1][0].split('=')[1].split(',')))
    robots[-1][1] = list(map(int, robots[-1][1].split('=')[1].split(',')))
f.close()
x_len, y_len = 101, 103
quad = [0,0,0,0]

for robot in robots:
    x = (robot[0][0] + 100 * robot[1][0]) % x_len
    y = (robot[0][1] + 100 * robot[1][1]) % y_len
    if x <= x_len // 2 - 1:
        if y <= y_len // 2 - 1:
            quad[0] += 1
        elif y_len // 2 + 1 <= y:
            quad[1] += 1
    elif x_len // 2 + 1 <= x:
        if y <= y_len // 2 - 1:
            quad[2] += 1
        elif y_len // 2 + 1 <= y:
            quad[3] += 1
safety_factor = 1
for q in quad:
    safety_factor *= q
print("Part 1:", safety_factor)

i = 0
while True:
    floor = []
    for j in range(y_len):
        floor.append([0] * x_len)
    for robot in robots:
        x = (robot[0][0] + i * robot[1][0]) % x_len
        y = (robot[0][1] + i * robot[1][1]) % y_len
        floor[y][x] += 1
    onTop = False
    for r in floor:
        for c in r:
            if c not in [0, 1]:
                onTop = True
                
    if not onTop:
        plt.imshow(floor, interpolation='none')
        plt.show()
        break
        
    i += 1
print("Part 2:", i)