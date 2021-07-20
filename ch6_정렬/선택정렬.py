# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 18:09:04 2021

@author: Jiyun
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j

    array[i], array[min_index] = array[min_index], array[i]
print(array)