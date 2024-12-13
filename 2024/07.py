# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:10:05 2024
"""
def cat(a, b):
    return int(str(a) + str(b))
def add(a, b):
    return a + b
def mul(a, b):
    return a * b

f = open("07.txt", 'r')
equations = []
for line in f.readlines():
    equations.append(line[:-1].split(":"))
    equations[-1][1] = list(map(int, equations[-1][1].split(" ")[1:]))
    equations[-1][0] = int(equations[-1][0])
f.close()

def check_op(n, eq):
    if len(eq) == 1:
        return int(n) == eq[0]
    
    for op in [add, mul]:
        if check_op(n, [op(eq[0], eq[1])] + eq[2:]):
            return n
    return False
    
def check_op_cat(n, eq):
    if len(eq) == 1:
        return int(n) == eq[0]
    
    for op in [add, mul, cat]:
        if check_op_cat(n, [op(eq[0], eq[1])] + eq[2:]):
            return n
    return False
    
res = 0
for eq in equations:
    if check_op(eq[0], eq[1]):
        res += eq[0]
print("Part 1:", res)

res = 0
for eq in equations:
    if check_op_cat(eq[0], eq[1]):
        res += eq[0]
print("Part 2:", res)
