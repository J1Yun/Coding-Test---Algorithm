n, m = map(int, input().split())
x, y, d = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
data[x][y] = 2

result = 1
while 1:
    i = 0
    for i in range(1, 5):
        temp_d = (d -i) % 4
        nx, ny = x + dx[temp_d], y + dy[temp_d]
        if data[nx][ny] == 0:
            x, y, d = nx, ny, temp_d
            result += 1
            data[x][y] = 2
            break 
    if i == 4:
        nx, ny = x + dx[d - 2], y + dy[d - 2]
        if data[nx][ny] != 1:
            x, y = nx, ny
        else:
            break

print(result)