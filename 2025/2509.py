# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 09:17:00 2025
"""
f = open("2509.txt", 'r')
data = f.read()
f.close()

data = [list(map(int, x.split(','))) for x in data[:-1].split('\n')]

def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

largest_area = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        largest_area = max(largest_area, area(data[i], data[j]))
print("Part 1:", largest_area)

edges = []
areas = []

for i in range(-1, len(data)-1):
    edges.append(sorted([data[i], data[i+1]]))
    for j in range(i+1, len(data)):
        areas.append([area(data[i], data[j]), min(data[i], data[j]), max(data[i], data[j])])
        
areas = sorted(areas)[::-1]
edges = sorted(edges, key=lambda x: area(x[0], x[1]))[::-1]

for rectangle in areas:
    size, x1, y1, x2, y2 = rectangle[0], rectangle[1][0], min(rectangle[1][1], rectangle[2][1]), rectangle[2][0], max(rectangle[1][1], rectangle[2][1])
    good_rectangle = True
    for (ex1, ey1), (ex2, ey2) in edges:
        if ex2 > x1 and ex1 < x2 and ey2 > y1 and ey1 < y2:
            good_rectangle = False
            
    if good_rectangle:
        print("Part 2:", size)
        break