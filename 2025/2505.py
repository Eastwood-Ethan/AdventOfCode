# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 13:03:06 2025
"""

f = open("2505.txt", 'r')
data = f.read()
f.close()

fresh_range, available_ingredient = data[:-1].split("\n\n")[0].split("\n"), data[:-1].split("\n\n")[1].split("\n")

fresh_ingredients = []
for r in fresh_range:
    start = int(r.split('-')[0])
    stop = int(r.split('-')[1])
    fresh_ingredients.append(range(start, stop + 1))
    
fresh_count = 0
for i in available_ingredient:
    for interval in fresh_ingredients:
        if int(i) in interval:
            fresh_count += 1
            break
        
print("Part 1:", fresh_count)

for i in range(len(fresh_range)):
    fresh_range[i] = [int(x) for x in fresh_range[i].split("-")]
    
fresh_range = sorted(fresh_range)
i = 0

while i < len(fresh_range) - 1:
    if fresh_range[i+1][0] <= fresh_range[i][1]:
        if fresh_range[i+1][1] >= fresh_range[i][1]:
            fresh_range[i][1] = fresh_range[i+1][1]
        fresh_range.pop(i+1)
    else:
        i += 1
    
fresh_ingredients = 0
for r in fresh_range:
    fresh_ingredients += r[1] - r[0] + 1
    
print("Part 2:", fresh_ingredients)