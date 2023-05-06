n, m = map(int, input().split())
graph = [[int(1e9)] * n for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] != int(1e9):
            count += 1
        if graph[j][i] != int(1e9):
            count += 1
    if count > n:
        result += 1

print(result)
