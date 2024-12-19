# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:23:09 2024
"""

f = open('19.txt', 'r')

towels, designs = f.read().split('\n\n')
towels = set(towels.split(', '))
designs = designs.split('\n')[:-1]

f.close()

def possibleDesign(design, towels):
    if design in towels:
        return True
    
    for i in range(1, len(design)):
        sub_design = design[:i]
        if sub_design in towels and possibleDesign(design[i:], towels):
            return True
    else:
        return False
    
num_possible = 0
for design in designs:
    num_possible += possibleDesign(design, towels)
print("Part 1:", num_possible)


def num_designs(design, towels, memo):
    if design in memo:
        return memo[design]
    
    num_ways = 0
    if design in towels:
        num_ways += 1
    
    for i in range(1, len(design)):
        sub_design = design[:i]
        if sub_design in towels:
            if design[i:] in memo:
                num_ways += memo[design[i:]]
            else:
                this_design = num_designs(design[i:], towels, memo)
                memo[design[i:]] = this_design
                num_ways += this_design
    
    return num_ways

num_ways = 0
for design in designs:
    num_ways += num_designs(design, towels, {})
print("Part 2:", num_ways)
