# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:54:26 2021

@author: Jiyun
"""

n, k = map(int, input().split())
count = 0

while(n>1):
    if n%k==0:
        n/=k
        count+=1
    else:
        n-=1
        count+=1

print(count)