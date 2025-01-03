# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 08:56:07 2024
"""
from collections import defaultdict

f = open('24.txt', 'r')
init_vals, equations = f.read().split('\n\n')
f.close()

init_vals, equations = init_vals.split('\n'), equations.split('\n')[:-1]
vals = defaultdict(int)
for line in init_vals:
    vals[line[:3]] = bool(int(line[-1]))
    

    
while len(vals) < len(init_vals) + len(equations):
    for line in equations:
        line = line.split(' ')
        if (line[-1] in vals) or (line[0] not in vals) or (line[2] not in vals):
            continue
        val1, val2 = bool(int(vals[line[0]])), bool(int(vals[line[2]]))
        if line[1] == 'AND':
            vals[line[-1]] = val1 and val2
        elif line[1] == 'OR':
            vals[line[-1]] = val1 or val2
        elif line[1] == 'XOR':
            vals[line[-1]] = ((not val1) and val2) or (val1 and (not val2))
        vals[line[-1]] = (vals[line[-1]])
        
    
i = 0
num = ''
while f'z{i:02d}' in vals:
    num = str(int(vals[f'z{i:02d}'])) + num 
    i += 1
    
print("Part 1:", int(num, 2))

eqn_res = {}
eqns = set()
for line in equations:
    line = line.split(" ")
    inputs = sorted([line[0], line[2]])
    toadd = inputs[0], line[1], inputs[1]
    eqns.add(toadd)
    eqn_res[toadd] = line[-1]
    
def find_result_loc(x, operator, y, gates):
    s, d = gates
    if (x, operator, y) in s:
        return d[(x, operator, y)]
    elif (y, operator, x) in s:
        return d[(y, operator, x)]
    else:
        return None
    
def swap(a, b, gates):
    s, d = gates
    for e in d:
        if d[e] == a:
            d[e] = b
        elif d[e] == b:
            d[e] = a
    return [s,d]

carry, swaps_made, b = None, [], 0
gates = [eqns, eqn_res]
while b < 45:
    x, y, z = f'x{b:02d}', f'y{b:02d}', f'z{b:02d}'
    
    if not b:
        carry = find_result_loc(x, 'AND', y, gates)
        b += 1
        continue
    
    AND_gate = find_result_loc(x, 'AND', y, gates)
    XOR_gate = find_result_loc(x, 'XOR', y, gates)
    
    carry_XOR_gate = find_result_loc(carry, 'XOR', XOR_gate, gates)
    if not carry_XOR_gate:
        b = 0
        gates = swap(AND_gate, XOR_gate, gates)
        swaps_made.append(AND_gate)
        swaps_made.append(XOR_gate)
        
    elif carry_XOR_gate != z:
        b = 0
        gates = swap(carry_XOR_gate, z, gates)
        swaps_made.append(carry_XOR_gate)
        swaps_made.append(z)
    else:
        carry_AND_gate = find_result_loc(carry, 'AND', XOR_gate, gates)
        carry = find_result_loc(carry_AND_gate, 'OR', AND_gate, gates)
        
        b += 1
        
print("Part 2:", ','.join(sorted(swaps_made)))
