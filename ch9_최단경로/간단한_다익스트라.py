# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 23:23:26 2021

@author: Jiyun
"""

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
print(graph)