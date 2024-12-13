# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:52:01 2024
"""

f = open("13.txt", 'r')
data = f.read().split('\n\n')
for i in range(len(data)):
    data[i] = data[i].splitlines()
    data[i][0] = [int(data[i][0][12:14]), int(data[i][0][18:20])]
    data[i][1] = [int(data[i][1][12:14]), int(data[i][1][18:20])]
    data[i][2] = data[i][2].split("=")[1:]
    data[i][2][0] = int(data[i][2][0][:-3])
    data[i][2][1] = int(data[i][2][1])
f.close()

# ax + by = m
# cx + dy = n
# Compute smith normal form?
# https://en.wikipedia.org/wiki/Diophantine_equation#System_of_linear_Diophantine_equations
# SNF of a b is gcd(a,b,c,d) 0
#        c d    0     |ad - bc|
# So B is that matrix
# Just need to use this https://en.wikipedia.org/wiki/Smith_normal_form#Algorithm