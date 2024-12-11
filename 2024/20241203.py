# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 09:34:46 2024
"""

f = open("20241203.txt", 'r')
data = f.readlines()
f.close()

def parse_memory(data, part2):
    mult_sum = 0
    enabled = True
    for line in data:
        i = 0
        while i < len(line) - 4:
            if line[i:i+4] == 'mul(':
                i += 4
                n1 = ''
                n2 = ''
                while line[i].isdigit():
                    n1 += line[i]
                    i += 1
                if n1 == '' or line[i] != ',':
                    continue
                i += 1
                while line[i].isdigit():
                    n2 += line[i]
                    i += 1
                if n2 == '' or line[i] != ')':
                    continue
                
                mult_sum += int(n1) * int(n2) * int(enabled)
            
                i += 1
            elif line[i:i+4] == 'do()'  and part2:
                enabled = True
                i += 4
            elif i < len(line) - 7 and line[i:i+7] == "don't()" and part2:
                enabled = False
                i += 7
            else:
                i += 1
                
    return mult_sum
        
print("Part 1:", parse_memory(data, False))
print("Part 2:", parse_memory(data, True))