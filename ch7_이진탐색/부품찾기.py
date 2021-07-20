# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:34:06 2021

@author: Jiyun
"""

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

for i in mlist:
    if i in nlist:
        print('yes', end=' ')
    else:
        print('no', end=' ')
