# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 20:01:40 2021

@author: Jiyun
"""

n, m, k = map(int, input().split());
num = list(map(int, input().split()))

num.sort()

a = num[n-1]
b = num[n-2]
result = 0

while(1):
    for i in range(k):
        if m==0:
            break
        result += a
        m -= 1
    if m==0:
        break
    result += b
    m -= 1

print(result)