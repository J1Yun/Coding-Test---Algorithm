# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:42:20 2021

@author: Jiyun
"""

from collections import deque

maps = []
n, m = map(int, input().split())
for i in range(n):
    maps.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x < 0 or new_y < 0 or new_x >= n or new_y >= m:
                continue
            if maps[new_x][new_y] == 1:
                maps[new_x][new_y] = maps[x][y] + 1
                queue.append((new_x, new_y))
            else:
                continue
                
bfs(0, 0)
print(maps[n-1][m-1])