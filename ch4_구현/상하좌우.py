# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 16:51:29 2021

@author: Jiyun
"""
x, y = 1, 1
n = int(input())
path = input().split() 

for i in path:
    if i == 'D':
        if x+1 <= n:
            x += 1
    elif i =='U':
        if x-1 >= 1:
            x -= 1
    elif i == 'R':
        if y+1 <= n:
            y += 1
    elif i == 'L':
        if y-1 >= 1:
            y -= 1
    else:
        continue

print(x, y)