# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:51:30 2024
"""

f = open("05.txt", 'r')
data = f.read().split('\n\n')
f.close()

updates = data[1].splitlines()
data[0] = data[0].splitlines()
for i in range(len(updates)):
    updates[i] = updates[i].split(',')
rules = []
for line in data[0]:
    rules.append(line.split('|'))

valid_sum = 0
invalid_sum = 0
for update in updates:
    valid = True
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if [update[j], update[i]] in rules:
                valid = False
                break
        if not valid:
            break
    if valid:
        valid_sum += int(update[len(update)//2])
        
    else:
        for i in range(len(update)):
            flipped = True
            while flipped:
                flipped = False
                for j in range(i+1, len(update)):
                    if [update[j], update[i]] in rules:
                        update[j], update[i] = update[i], update[j]
                        flipped = True
        
        invalid_sum += int(update[len(update)//2])
        
print("Part 1:", valid_sum)
print("Part 2:", invalid_sum)
