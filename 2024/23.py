# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 10:06:02 2024
"""
from collections import defaultdict
f = open('23.txt', 'r')
data = f.readlines()
f.close()
links = defaultdict(set)
computers = set()
for line in data:
    vals = line[:-1].split('-')
    links[vals[0]].add(vals[1])
    links[vals[1]].add(vals[0])
    computers.add(vals[0])
    computers.add(vals[1])
    
three_pairs = []
for first_val in links:
    for second_val in links[first_val]:
        for third_val in links[second_val]:
            if first_val in links[third_val]:
                if 't' == first_val[0] or 't' == second_val[0] or 't' == third_val[0]:
                    three_pairs.append([first_val, second_val, third_val])
                    
print("Part 1:", len(three_pairs) // 6)


def bronKerbosch(R, P, X, G, C):
    if not P and not X:
        if len(R) > 2:
            C.append(sorted(R))
        return
    
    for v in P | set():
        bronKerbosch(R | {v}, P & G[v], X & G[v], G, C)
        P.remove(v)
        X.add(v)
    
C = []
bronKerbosch(set(), computers, set(), links, C)
maxLenGroup = []
for group in C:
    if len(group) > len(maxLenGroup):
        maxLenGroup = group
print("Part 2:", ','.join(maxLenGroup))
