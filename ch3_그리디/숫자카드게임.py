# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:38:48 2021

@author: Jiyun
"""
min_line =[]

n, m = map(int, input().split())
for i in range(n):
    num = list(map(int, input().split()))
    min_line.append(min(num))

print(max(min_line))
