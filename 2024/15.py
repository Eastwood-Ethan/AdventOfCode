# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:23:42 2024
"""

f = open("15.txt", 'r')
data = f.read().split('\n')
f.close()

warehouse = []
movements = ''
robot = (-1, -1)
for i in range(len(data)):
    if data[i] and data[i][0] == '#':
        warehouse.append(list(data[i]))
        if '@' in data[i]:
            robot = (i, data[i].index('@'))
    elif data[i]:
        movements += data[i]
        
new_robot = (robot[0], 2 * robot[1])
new_warehouse = []
for r in range(len(warehouse)):
    new_warehouse.append([])
    for c in range(len(warehouse[0])):
        if warehouse[r][c] == 'O':
            new_warehouse[r] += ['[', ']']
        elif warehouse[r][c] == '@':
            new_warehouse[r] += ['@', '.']
        else:
            new_warehouse[r] += warehouse[r][c] * 2
        
dirs = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)}
for m in movements:
    next_pos = (robot[0] + dirs[m][0], robot[1] + dirs[m][1])
    if warehouse[next_pos[0]][next_pos[1]] == '#':
        continue
    if warehouse[next_pos[0]][next_pos[1]] == '.':
        warehouse[robot[0]][robot[1]] = '.'
        warehouse[next_pos[0]][next_pos[1]] = '@'
        robot = next_pos
    else:
        first_pos = next_pos
        while warehouse[next_pos[0]][next_pos[1]] == 'O':
            next_pos = (next_pos[0] + dirs[m][0], next_pos[1] + dirs[m][1])
            
        if warehouse[next_pos[0]][next_pos[1]] == '.':
            warehouse[next_pos[0]][next_pos[1]] = 'O'
            warehouse[first_pos[0]][first_pos[1]] = '@'
            warehouse[robot[0]][robot[1]] = '.'
            robot = first_pos

GPS = 0
for r in range(len(warehouse)):
    for c in range(len(warehouse[0])):
        if warehouse[r][c] == 'O':
            GPS += 100 * r + c
print("Part 1:", GPS)

def canPush(warehouse, next_pos, m):
    
    if warehouse[next_pos[0]][next_pos[1]] == '[':
        left_side = next_pos
        right_side = (next_pos[0], next_pos[1] + 1)
    elif warehouse[next_pos[0]][next_pos[1]] == ']':
        right_side = next_pos
        left_side = (next_pos[0], next_pos[1] - 1)
    else:
        raise Exception("Box not found?")
    canPushLeft, canPushRight = False, False
    if warehouse[left_side[0] + dirs[m][0]][left_side[1] + dirs[m][1]] == '.':
        canPushLeft = True
    elif warehouse[left_side[0] + dirs[m][0]][left_side[1] + dirs[m][1]] in ['[', ']']:
        canPushLeft = canPush(warehouse, (left_side[0] + dirs[m][0], left_side[1] + dirs[m][1]), m)
        
        
    if warehouse[right_side[0] + dirs[m][0]][right_side[1] + dirs[m][1]] == '.':
        canPushRight = True
    elif warehouse[right_side[0] + dirs[m][0]][right_side[1] + dirs[m][1]] in ['[', ']']:
        canPushRight = canPush(warehouse, (right_side[0] + dirs[m][0], right_side[1] + dirs[m][1]), m)

    return canPushLeft and canPushRight

def push(warehouse, next_pos, m):
    if not canPush(warehouse, next_pos, m):
        raise Exception("Trying to push a box into a wall")
        
    if warehouse[next_pos[0]][next_pos[1]] == '[':
        left_side = next_pos
        right_side = (next_pos[0], next_pos[1] + 1)
    elif warehouse[next_pos[0]][next_pos[1]] == ']':
        right_side = next_pos
        left_side = (next_pos[0], next_pos[1] - 1)
    else:
        raise Exception("Box not found?")
        
    if warehouse[left_side[0] + dirs[m][0]][left_side[1] + dirs[m][1]] in ['[', ']']:
        warehouse = push(warehouse, (left_side[0] + dirs[m][0], left_side[1] + dirs[m][1]), m)
        
    if warehouse[right_side[0] + dirs[m][0]][right_side[1] + dirs[m][1]] in ['[', ']']:
        warehouse = push(warehouse, (right_side[0] + dirs[m][0], right_side[1] + dirs[m][1]), m)
        
    if (warehouse[left_side[0] + dirs[m][0]][left_side[1] + dirs[m][1]] == '.' and 
       warehouse[right_side[0] + dirs[m][0]][right_side[1] + dirs[m][1]] == '.'):
        warehouse[left_side[0] + dirs[m][0]][left_side[1] + dirs[m][1]] = '['
        warehouse[right_side[0] + dirs[m][0]][right_side[1] + dirs[m][1]] = ']'
        warehouse[left_side[0]][left_side[1]] = '.'
        warehouse[right_side[0]][right_side[1]] = '.'
        
    return warehouse

robot = new_robot
warehouse = new_warehouse
for m in movements:
    next_pos = (robot[0] + dirs[m][0], robot[1] + dirs[m][1])
    if warehouse[next_pos[0]][next_pos[1]] == '#':
        continue
    if warehouse[next_pos[0]][next_pos[1]] == '.':
        warehouse[robot[0]][robot[1]] = '.'
        warehouse[next_pos[0]][next_pos[1]] = '@'
        robot = next_pos
    else:
        if m in ['^', 'v']:
            if canPush(warehouse, next_pos, m):
                warehouse = push(warehouse, next_pos, m)
                warehouse[next_pos[0]][next_pos[1]] = '@'
                warehouse[robot[0]][robot[1]] = '.'
                robot = next_pos
        else:
            first_pos = next_pos
            while warehouse[next_pos[0]][next_pos[1]] in ['[', ']']:
                next_pos = (next_pos[0] + dirs[m][0], next_pos[1] + dirs[m][1])
                
            if warehouse[next_pos[0]][next_pos[1]] == '.':
                if m == '>':
                    for i in range(first_pos[1] + 1, next_pos[1] + 1, 2):
                        warehouse[next_pos[0]][i] = '['
                        warehouse[next_pos[0]][i + 1] = ']'
                else:
                    for i in range(next_pos[1], first_pos[1], 2):
                        warehouse[next_pos[0]][i] = '['
                        warehouse[next_pos[0]][i + 1] = ']'
                
                warehouse[first_pos[0]][first_pos[1]] = '@'
                warehouse[robot[0]][robot[1]] = '.'
                robot = first_pos
            
GPS = 0
for r in range(len(warehouse)):
    for c in range(len(warehouse[0])):
        if warehouse[r][c] == '[':
            GPS += 100 * r + c
# for line in new_warehouse:
#     print("".join(line))
print("Part 2:", GPS)