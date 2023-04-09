from collections import deque

n = int(input())
k = int(input())

data = [[0]*n for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    data[a-1][b-1] = -1
l = int(input())
command = deque()
for _ in range(l):
    a, b = map(str, input().split())
    command.append((int(a), b))

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
rotation = {'L': -1, 'D': 1}
d, t = 0, 1
data[0][0] = 1
snake = deque([(0, 0)])

while 1:
    nx, ny = snake[-1][0] + dx[d], snake[-1][1] + dy[d]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or data[nx][ny] == 1:
        break
    if data[nx][ny] == 0:
        xx, yy = snake.popleft()
        data[xx][yy] = 0
    data[nx][ny] = 1
    snake.append((nx, ny))

    if command and t == command[0][0]:
        d = (d + rotation[command[0][1]]) % 4
        command.popleft()
    t += 1

print(t)