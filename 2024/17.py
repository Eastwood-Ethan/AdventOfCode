# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:31:31 2024
"""

f = open("17.txt", 'r')
data = f.read().split('\n')
f.close()

reg = []
for i in range(3): reg.append(int(data[i].split(" ")[-1]))

inst = data[4].split(',')
inst[0] = inst[0][-1]
inst = list(map(int, inst))

def machine(inst, reg):
    reg = reg[:]
    i = 0
    output = []
    while i < len(inst) - 1:
        
        oc = inst[i]
        
        op = inst[i + 1]
        combo = 0
        if op in [4, 5, 6]:
            idx = [4, 5, 6].index(op)
            combo = reg[idx]
        else:
            combo = op
            
        match oc:
            case 0:
                reg[0] = reg[0] // (2 ** combo)
            case 1:
                reg[1] = reg[1] ^ op 
            case 2:
                reg[1] = combo % 8
            case 3:
                if reg[0]:
                    i = op - 2
            case 4:
                reg[1] = reg[1] ^ reg[2]
            case 5:
                output.append(combo % 8)
            case 6:
                reg[1] = reg[0] // (2 ** combo)
            case 7:
                reg[2] = reg[0] // (2 ** combo)
        
        i += 2
    return output

print("Part 1:", ','.join(list(map(str, machine(inst, reg)))))

reg[0], output = 0, machine(inst, reg)
while output != inst:
    
    if output == inst[-len(output):]:
        reg[0] *= 8
    else:
        reg[0] += 1
        
    output = output = machine(inst, reg)
        
print("Part 2:", reg[0])
        