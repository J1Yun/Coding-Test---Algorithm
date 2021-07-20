n, m = map(int, input().split())
x, y, d = map(int, input().split())
visit = [[0]*m for _ in range(n)]
visited = [[0]*m]*n
print(visit)
print(visited)

game = []
for _ in range(n):
    game.append(list(map(int, input().split())))
    
visit[x][y] = 1
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
count = 0
result = 1
while 1:
    d = (d + 3) % 4
    dx = x + move[d][0]
    dy = y + move[d][1]
    print(dx, dy)
    print(visit)
    if visit[dx][dy] == 0 and game[dx][dy] == 0:
        x = dx
        y = dy
        visit[x][y] = 1
        count = 0
        result += 1
        continue
    else:
        count += 1
    
    if count == 4:
        dx = x + move[(d+2)%4][0]
        dy = y + move[(d+2)%4][1]
        if game[dx][dy] == 1:
            break
        x = dx
        y = dy
        count = 0
print(visit)
print(result)