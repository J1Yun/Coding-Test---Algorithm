# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:09:07 2021

@author: Jiyun
"""

n = int(input())

array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))

array = sorted(array, key = lambda student: student[1])

for i in array:
    print(i[0], end=' ')