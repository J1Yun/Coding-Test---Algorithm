# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 20:21:21 2021

@author: Jiyun
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 1
end = max(array)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    length_sum = 0
    for i in array:
        if i > mid:
            length_sum += (i-mid)
    
    if length_sum < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1
        
print(result)