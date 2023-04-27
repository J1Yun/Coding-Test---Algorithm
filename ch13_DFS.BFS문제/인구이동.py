from collections import deque

n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(x, y):
    global array

    queue = deque()
    visited[x][y] = 1
    queue.append((x, y))
    count, summary = 1, data[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue

            if l <= abs(data[x][y] - data[nx][ny]) <= r:
                queue.append((nx, ny))
                visited[nx][ny] = 1
                count += 1
                summary += data[nx][ny]
                array.append((nx, ny))

    return count, summary

flag, result = True, 0
while flag:
    flag = False
    result += 1

    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                array = [(i, j)]
                count, summary = bfs(i, j)
                if count > 1:
                    flag = True
                    for x, y in array:
                        data[x][y] = summary // count

print(result-1)
            
