from itertools import combinations
from collections import deque

n = int(input())
data = []

for _ in range(n):
    data.append(list(map(str, input().split())))

empty, teacher = [], []
for i in range(n):
    for j in range(n):
        if data[i][j] == 'X':
            empty.append((i, j))
        elif data[i][j] == 'T':
            teacher.append((i, j))

obstacle = list(combinations(empty, 3))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    queue = deque([(x, y, 0), (x, y, 1), (x, y, 2), (x, y, 3)])

    while queue:
        x, y, d = queue.popleft()
        nx, ny = x + dx[d], y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
            continue
        if data[nx][ny] == 'X':
            queue.append((nx, ny, d))
            visited[nx][ny] = 1
        elif data[nx][ny] == 'S':
            return False

    return True

answer = 'NO'
for obs in obstacle:
    for x, y in obs:
        data[x][y] = 'O'

    result = True

    for x, y in teacher:
        if not bfs(x, y):
            result = False
            break
    if result:
        answer = 'YES'
        break

    for x, y in obs:
        data[x][y] = 'X'

print(answer)