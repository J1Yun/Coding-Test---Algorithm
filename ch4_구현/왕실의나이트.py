# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:36:35 2021

@author: Jiyun
"""

l = input()
row = int(l[1])
column = ord(l[0])

step = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

count = 0
for s in step:
    next_row = row + s[0]
    next_column = chr(column + s[1])
    if next_row >= 1 and next_row <= 8 and next_column >= 'a' and next_column <= 'h':
        count += 1
        
print(count)