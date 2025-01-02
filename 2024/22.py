# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 09:55:36 2024
"""
from collections import deque, defaultdict
f = open('22.txt', 'r')
prices = f.readlines()
f.close()

prices = list(map(int, prices))

for i in range(len(prices)):
    for j in range(2000):
        prices[i] = ((prices[i] * 64) ^ prices[i]) % 2**24
        prices[i] = ((prices[i] // 32) ^ prices[i]) % 2**24
        prices[i] = ((prices[i] * 2048) ^ prices[i]) % 2**24
        
print("Part 1:", sum(prices))


f = open('22.txt', 'r')
prices = f.readlines()
f.close()

initial_prices = list(map(int, prices))
prices = []
changes = []

for i in range(len(initial_prices)):
    changes.append([])
    prices.append([initial_prices[i]])
    for j in range(2000):
        initial_prices[i] = ((initial_prices[i] * 64) ^ initial_prices[i]) % 2**24
        initial_prices[i] = ((initial_prices[i] // 32) ^ initial_prices[i]) % 2**24
        initial_prices[i] = ((initial_prices[i] * 2048) ^ initial_prices[i]) % 2**24
        prices[-1].append(initial_prices[i] % 10)
        
        changes[-1].append((prices[-1][j] - prices[-1][j - 1], prices[-1][j]))
        
DP = defaultdict(int)
for monkey in range(len(prices)):
    seq_seen = set()
    cur_seq = deque([])
    for c in range(len(changes[0])):
        
        if c < 4:
            cur_seq.append(changes[monkey][c][0])
            continue
        
        if tuple(cur_seq) not in seq_seen:
            DP[tuple(cur_seq)] += changes[monkey][c-1][1]
        
        seq_seen.add(tuple(cur_seq))
        cur_seq.append(changes[monkey][c][0])
        cur_seq.popleft()
        
print("Part 2:", DP[max(DP, key=DP.get)])
