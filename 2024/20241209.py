# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:10:03 2024
"""

f = open("20241209.txt", 'r')
disk_map = f.read()[:-1]
f.close()

def update_first_blank(disk_space, left_blank):
    while disk_space[left_blank] != '.':
        left_blank += 1
    return left_blank

def update_last_num_part1(disk_space, right_num):
    while disk_space[right_num] == '.':
        right_num -= 1
    return right_num

def find_first_blank(disk_space, n, idx_tomove):
    i = 0
    len_blank = 0
    while i < idx_tomove and len_blank < n:
        if disk_space[i] != '.':
            len_blank = 0
        else:
            len_blank += 1
        i += 1
    return i - len_blank if len_blank == n else -1

def find_len_num(disk_space, idx):
    i = idx
    while i < len(disk_space) and disk_space[i] == disk_space[idx]:
        i += 1
        
    return i - idx

def update_last_num_part2(disk_space, right_num):
    while disk_space[right_num] == '.' and right_num >= 0:
        right_num -= 1
    right_side = right_num
    while disk_space[right_num] == disk_space[right_side] and right_num >= 0:
        right_num -= 1
    return right_num + 1

def compact_disk_space(disk_map, part2):
    disk_space = []
    for i in range(0, len(disk_map), 2):
        disk_space += [i // 2] * int(disk_map[i])
        if i == len(disk_map) - 1:
            break
        disk_space += ['.'] * int(disk_map[i + 1])
    
    if not part2:
        left_blank = update_first_blank(disk_space, 0)
        right_num = update_last_num_part1(disk_space, len(disk_space) - 1)
    
        while left_blank < right_num:
            disk_space[left_blank], disk_space[right_num] = disk_space[right_num], disk_space[left_blank]
            
            left_blank = update_first_blank(disk_space, left_blank)
            right_num = update_last_num_part1(disk_space, right_num)
    
    else:
        right_num = update_last_num_part2(disk_space, len(disk_space) - 1)
        n = find_len_num(disk_space, right_num)
        first_blank = find_first_blank(disk_space, n, right_num)
    
        while right_num > 1:
            if first_blank == -1:
                right_num -= 1
            else:
                for i in range(n):
                    disk_space[first_blank + i], disk_space[right_num + i] = disk_space[right_num + i], disk_space[first_blank + i]
            
            right_num = update_last_num_part2(disk_space, right_num)
            n = find_len_num(disk_space, right_num)
            first_blank = find_first_blank(disk_space, n, right_num)
        
    checksum = 0
    for i in range(len(disk_space)):
        if disk_space[i] != '.':
            checksum += i * disk_space[i]
    return checksum

print("Part 1:", compact_disk_space(disk_map, False))
print("Part 2:", compact_disk_space(disk_map, True))