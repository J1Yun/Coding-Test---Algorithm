# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 17:40:19 2021

@author: Jiyun
"""

n = int(input())
d = [0] * (n+1)

d[1] = 1
if n > 1:
    d[2] = 3

for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2] * 2 )%10007
    
print(d[n])