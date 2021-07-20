# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 17:19:16 2021

 @author: Jiyun
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range (k):
    if a[i] < b[i]:                                                                                                                                                                                                                                                                                             
        a[i], b[i] = b[i], a[i]
    else:
        break                                                                                                                                                              

print(sum(a))