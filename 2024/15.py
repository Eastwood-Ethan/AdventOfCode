# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 12:23:42 2024
"""

f = open("15.txt", 'r')
data = f.read().split('\n')
f.close()

warehouse = []
movements = ''
robot = 0
for i in range(len(data)):
    if data[i] and data[i][0] == '#':
        warehouse.append(list(data[i]))
        if '@' in data[i]:
            robot = i + data[i].index('@') * 1j
    elif data[i]:
        movements += data[i]
        
new_robot = robot.real + 2 * robot.imag * 1j
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
        
dirs = {'^':-1, '>':1j, 'v':1, '<':-1j}
for m in movements:
    next_pos = robot + dirs[m]
    if warehouse[int(next_pos.real)][int(next_pos.imag)] == '#':
        continue
    if warehouse[int(next_pos.real)][int(next_pos.imag)] == '.':
        warehouse[int(robot.real)][int(robot.imag)] = '.'
        warehouse[int(next_pos.real)][int(next_pos.imag)] = '@'
        robot = next_pos
    else:
        first_pos = next_pos
        while warehouse[int(next_pos.real)][int(next_pos.imag)] == 'O':
            next_pos += dirs[m]
            
        if warehouse[int(next_pos.real)][int(next_pos.imag)] == '.':
            warehouse[int(next_pos.real)][int(next_pos.imag)] = 'O'
            warehouse[int(first_pos.real)][int(first_pos.imag)] = '@'
            warehouse[int(robot.real)][int(robot.imag)] = '.'
            robot = first_pos

GPS = 0
for r in range(len(warehouse)):
    for c in range(len(warehouse[0])):
        if warehouse[r][c] == 'O':
            GPS += 100 * r + c
print("Part 1:", GPS)

def canPush(warehouse, next_pos, m):
    
    if warehouse[int(next_pos.real)][int(next_pos.imag)] == '[':
        left_side = next_pos
        right_side = next_pos + 1j
    elif warehouse[int(next_pos.real)][int(next_pos.imag)] == ']':
        right_side = next_pos
        left_side = next_pos - 1j
    else:
        raise Exception("Box not found?")
    canPushLeft, canPushRight = False, False
    next_left = left_side + dirs[m]
    if warehouse[int(next_left.real)][int(next_left.imag)] == '.':
        canPushLeft = True
    elif warehouse[int(next_left.real)][int(next_left.imag)] in ['[', ']']:
        canPushLeft = canPush(warehouse, next_left, m)
        
    next_right = right_side + dirs[m]
    if warehouse[int(next_right.real)][int(next_right.imag)] == '.':
        canPushRight = True
    elif warehouse[int(next_right.real)][int(next_right.imag)] in ['[', ']']:
        canPushRight = canPush(warehouse, next_right, m)

    return canPushLeft and canPushRight

def push(warehouse, next_pos, m):
    if not canPush(warehouse, next_pos, m):
        raise Exception("Trying to push a box into a wall")
        
    if warehouse[int(next_pos.real)][int(next_pos.imag)] == '[':
        left_side = next_pos
        right_side = next_pos + 1j
    elif warehouse[int(next_pos.real)][int(next_pos.imag)] == ']':
        right_side = next_pos
        left_side = next_pos - 1j
    else:
        raise Exception("Box not found?")
    next_left = left_side + dirs[m]
    if warehouse[int(next_left.real)][int(next_left.imag)] in ['[', ']']:
        warehouse = push(warehouse, next_left, m)
    next_right = right_side + dirs[m]
    if warehouse[int(next_right.real)][int(next_right.imag)] in ['[', ']']:
        warehouse = push(warehouse, next_right, m)
        
    if (warehouse[int(next_left.real)][int(next_left.imag)] == '.' and 
       warehouse[int(next_right.real)][int(next_right.imag)] == '.'):
        warehouse[int(next_left.real)][int(next_left.imag)] = '['
        warehouse[int(next_right.real)][int(next_right.imag)] = ']'
        warehouse[int(left_side.real)][int(left_side.imag)] = '.'
        warehouse[int(right_side.real)][int(right_side.imag)] = '.'
        
    return warehouse

robot = new_robot
warehouse = new_warehouse
for m in movements:
    next_pos = robot + dirs[m]
    
    if warehouse[int(next_pos.real)][int(next_pos.imag)] == '#':
        continue
    if warehouse[int(next_pos.real)][int(next_pos.imag)] == '.':
        warehouse[int(robot.real)][int(robot.imag)] = '.'
        warehouse[int(next_pos.real)][int(next_pos.imag)] = '@'
        robot = next_pos
    else:
        if m in ['^', 'v']:
            if canPush(warehouse, next_pos, m):
                warehouse = push(warehouse, next_pos, m)
                warehouse[int(next_pos.real)][int(next_pos.imag)] = '@'
                warehouse[int(robot.real)][int(robot.imag)] = '.'
                robot = next_pos
        else:
            first_pos = next_pos
            while warehouse[int(next_pos.real)][int(next_pos.imag)] in ['[', ']']:
                next_pos += dirs[m]
                
            if warehouse[int(next_pos.real)][int(next_pos.imag)] == '.':
                if m == '>':
                    for i in range(int(first_pos.imag) + 1, int(next_pos.imag) + 1, 2):
                        warehouse[int(next_pos.real)][i] = '['
                        warehouse[int(next_pos.real)][i + 1] = ']'
                else:
                    for i in range(int(next_pos.imag), int(first_pos.imag), 2):
                        warehouse[int(next_pos.real)][i] = '['
                        warehouse[int(next_pos.real)][i + 1] = ']'
                
                warehouse[int(first_pos.real)][int(first_pos.imag)] = '@'
                warehouse[int(robot.real)][int(robot.imag)] = '.'
                robot = first_pos
            
GPS = 0
for r in range(len(warehouse)):
    for c in range(len(warehouse[0])):
        if warehouse[r][c] == '[':
            GPS += 100 * r + c
# for line in new_warehouse:
#     print("".join(line))
print("Part 2:", GPS)
