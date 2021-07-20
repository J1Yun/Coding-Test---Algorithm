# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:53:36 2021

@author: Jiyun
"""

from collections import deque

def bfs(graph, s, visited):
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],
    [2, 3, 8],                                                                       
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]    
]

visited = [False] * 9

bfs(graph, 1, visited)