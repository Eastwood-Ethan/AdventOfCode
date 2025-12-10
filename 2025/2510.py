# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 12:31:32 2025
"""
f = open("2510.txt", 'r')
data = f.read()
f.close()
from collections import deque
from scipy.optimize import linprog

data = data[:-1].split('\n')
for i in range(len(data)):
    machine = data[i]
    lights = list(machine.split(']')[0][1:])
    n = len(lights)
    new_lights = ''
    for j in range(len(lights)):
        if lights[j] == '.':
            new_lights += '0'
        else:
            new_lights += '1'
    lights = int("".join(new_lights), 2)
    
    
    buttons = machine.split('] ')[1].split(' {')[0].split(" ")
    new_buttons = []
    for j in range(len(buttons)):
        buttons[j] = buttons[j][1:-1].split(',')
        new_buttons.append('')
        for k in range(n):
            if str(k) in buttons[j]:
                new_buttons[-1] += '1'
            else:
                new_buttons[-1] += '0'
        new_buttons[-1] = int(new_buttons[-1], 2)
        buttons[j] = list(map(int, buttons[j]))
    
    joltage = list(map(int, machine.split('{')[1][:-1].split(',')))
    
    data[i] = [lights, new_buttons, buttons, joltage]
    
presses = 0

for light, buttons, _, _ in data:
    queue = deque([[0, 0]]) # [light, switches to arrive at this position]
    memo = {0:0}
    
    while queue or (not light in memo):
        for b in buttons:
            after_press = queue[0][0] ^ b 
            if after_press not in memo:
                memo[after_press] = queue[0][1] + 1
                queue.append([after_press, queue[0][1] + 1])
        queue.popleft()
                    
    presses += memo[light]
    
print("Part 1:", presses)

def optimizer(buttons, joltages):
    A = []
    for i in range(len(joltages)):
        a = []
        for b in buttons:
            if i in b:
                a.append(1)
            else:
                a.append(0)
        A.append(a)
        
    return round(linprog([1]*len(buttons), 
                         A_eq= A,
                         b_eq=joltages,
                         integrality=True).fun)


presses = 0
for i in range(len(data)):
    presses += optimizer(data[i][2], data[i][3])

print("Part 2:", presses)