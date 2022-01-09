# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 23:16:14 2021

@author: Jiyun
"""

n, k = map(int, input().split())
result = 0

while 1:
    if n<k:
        break
    target = (n//k)*k
    result += (n-target)
    n=target
    result +=1
    n //= k

result += (n-1)
print(result)