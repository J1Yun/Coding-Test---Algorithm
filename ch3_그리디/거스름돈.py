# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 16:43:52 2021

@author: Jiyun
"""

coin = [500, 100, 50, 10]
count = 0

n = int(input());

for c in coin :
    count += n // c
    n %= c

print(count)