# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:43:52 2021

@author: Jiyun
"""

n = int(input())
array = list(map(int, input().split()))

d = [0] * n

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+array[i])

print(d[n-1])