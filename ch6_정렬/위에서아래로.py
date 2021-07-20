# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 16:58:33 2021

@author: Jiyun
"""

n = int(input())

array =[]
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)
for i in array:
    print(i, end=' ')