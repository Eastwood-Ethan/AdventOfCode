# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 15:52:01 2024
"""
from smithnormalform import matrix, snfproblem, z
from sympy import symbols, Eq, solve

f = open("13.txt", 'r')
data = f.read().split('\n\n')
for i in range(len(data)):
    data[i] = data[i].splitlines()
    data[i][0] = [int(data[i][0][12:14]), int(data[i][0][18:20])]
    data[i][1] = [int(data[i][1][12:14]), int(data[i][1][18:20])]
    data[i][2] = data[i][2].split("=")[1:]
    data[i][2][0] = int(data[i][2][0][:-3])
    data[i][2][1] = int(data[i][2][1])
    data[i][0][1], data[i][1][0] = data[i][1][0], data[i][0][1]
f.close()

tokens = 0
for m in data:
    A = matrix.Matrix(2, 2, [z.Z(m[0][0]), z.Z(m[0][1]), z.Z(m[1][0]), z.Z(m[1][1])])
    C = matrix.Matrix(2, 1, [z.Z(m[2][0]), z.Z(m[2][1])])
    snf = snfproblem.SNFProblem(A)
    snf.computeSNF()
    D = snf.S.__mul__(C)
    DoB = [float(str(D.elements[0])) / float(str(snf.J.elements[0])), 
          float(str(D.elements[1])) / float(str(snf.J.elements[3]))]
    
    if not (DoB[0].is_integer() and DoB[1].is_integer()):
        continue
    DoB = matrix.Matrix(2, 1, [z.Z(int(DoB[0])), z.Z(int(DoB[1]))])
    sol = snf.T.__mul__(DoB)
    tokens += 3 * int(str(sol.elements[0])) + int(str(sol.elements[1]))

print("Part 1:", tokens)

tokens = 0
h = 10000000000000
# Floating point issues needs sympy
for m in data:
    b1, b2 = symbols('b1 b2', integer=True)
    button_1 = Eq(m[0][0] * b1 + m[0][1] * b2, m[2][0] + h)
    button_2 = Eq(m[1][0] * b1 + m[1][1] * b2, m[2][1] + h)
    
    sol = solve((button_1, button_2), (b1, b2))
    
    if sol and sol[b1].is_integer and sol[b2].is_integer:
        tokens += 3 * int(sol[b1]) + int(sol[b2])

print("Part 2:", tokens)
