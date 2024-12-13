# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:07:55 2024
"""
from collections import defaultdict

f = open("11.txt", 'r')
stones = list(map(int, f.read()[:-1].split(" ")))
f.close()

def blink(stones, n):
    stone_dict = defaultdict(int)
    for s in stones:
        stone_dict[s] += 1
    stones = stone_dict
    
    blink_results = defaultdict(int)
    blink_results[0] = 1
    
    #no need to keep in order!
    for _ in range(n):
        next_stones = defaultdict(int)
        for s in stones:
            if s in blink_results:
                if type(blink_results[s]) == list:
                    next_stones[blink_results[s][0]] += stones[s]
                    next_stones[blink_results[s][1]] += stones[s]
                else:
                    next_stones[blink_results[s]] += stones[s]
                    
            elif len(str(s)) % 2 == 0:
                l = len(str(s))
                res1 = s % (10 ** (l // 2))
                res2 = s // (10 ** (l // 2))
                blink_results[s] = [res1, res2]
                next_stones[blink_results[s][0]] += int(stones[s])
                next_stones[blink_results[s][1]] += int(stones[s])
                
            else:
                res = s * 2024
                blink_results[s] = res
                next_stones[blink_results[s]] += stones[s]
                
        stones = next_stones
    num_stones = 0
    for s in stones:
        num_stones += stones[s]
        
    return num_stones

print("Part 1:", blink(stones, 25))
print("Part 2:", blink(stones, 75))
