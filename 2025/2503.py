# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 08:54:50 2025
"""
f = open("2503.txt", 'r')
data = f.read()
f.close()

data = data[:-1].split("\n")

joltage = 0
for b in data:
    first_num = max(b[:-1])
    second_num = max(b[b.find(first_num) + 1:])
    joltage += int(first_num) * 10 + int(second_num)
    
print("Part 1:", joltage)

joltages = 0
for b in data:
    joltage = ""
    for i in range(12):
        next_battery = max(b[:len(b)-(11-i)])
        b = b[b.find(next_battery) + 1:]
        joltage += next_battery
        
    joltages += int(joltage)
print("Part 2:", joltages)