# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 18:34:38 2021

@author: Jiyun
"""
n = int(input())

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(n))