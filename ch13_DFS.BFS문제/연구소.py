from itertools import combinations
from copy import deepcopy

n, m = map(int, input().split())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

wall = []
virus = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            wall.append((i, j))
        elif data[i][j] == 2:
            virus.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    for t in range(4):
        nx, ny = x + dx[t], y + dy[t]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if temp_data[nx][ny] == 0:
            temp_data[nx][ny] = 2
            dfs(nx, ny)

def check():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp_data[i][j] == 0:
                count += 1
    return count

wall = list(combinations(wall, 3))
result = 0

for comb in wall:
    temp_data = deepcopy(data)
    for a, b in comb:
        temp_data[a][b] = 1

    for a, b in virus:
        dfs(a, b)

    result = max(result, check())

print(result)