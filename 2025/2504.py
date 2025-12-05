# -*- coding: utf-8 -*-
"""
Created on Fri Dec  5 12:42:50 2025
"""

f = open("2504.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split("\n")
rows, columns = len(data), len(data[0])
new_data = []
new_data.append(["."] * (columns + 2))
for r in range(rows):
    new_data.append(["."] + list(data[r]) + ["."])
new_data.append(["."] * (columns + 2))
data = new_data

forklift = 0
for r in range(1, rows+1):
    for c in range(1, columns+1):
        if data[r][c] == "@":
            rolls = 0
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if x != 0 or y != 0:
                        if data[r + x][c + y] == "@":
                            rolls += 1
            if rolls < 4:
                forklift += 1
                
print("Part 1:", forklift)

forklift = 0
found_movable_roll = True
while found_movable_roll:
    found_movable_roll = False
    for r in range(1, rows+1):
        for c in range(1, columns+1):
            if data[r][c] == "@":
                rolls = 0
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x != 0 or y != 0:
                            if data[r + x][c + y] == "@":
                                rolls += 1
                if rolls < 4:
                    found_movable_roll = True
                    forklift += 1
                    data[r][c] = '.'
print("Part 2:", forklift)
                    
    
                
