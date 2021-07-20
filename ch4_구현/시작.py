# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:28:12 2021

@author: Jiyun
"""

n = int(input())
count = 0

for i in range (n+1):
    for j in range (60):
        for k in range (60):
            if '3' in str(i)+str(j)+str(k):
                count += 1
                
print(count)