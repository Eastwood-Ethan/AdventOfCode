# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 13:41:25 2025
"""

f = open("2501.txt", 'r')
data = f.read()
f.close()

rotations = data.split("\n")[:-1]

password_a = 0
password_b = 0
dial = 50

for r in rotations:
    dial_start = dial
    move = int(r[1:])
    password_b += move // 100
    move %= 100
    
    if r[0] == 'L':
        dial -= move
    else:
        dial += move
        
    if (dial <= 0 or dial >= 100) and dial_start != 0:
        password_b += 1
    dial %= 100
    if dial == 0:
        password_a += 1
        
print("Part 1:", password_a)
print("Part 2:", password_b)
