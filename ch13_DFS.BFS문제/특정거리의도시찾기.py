from collections import deque

n, m, k, x = map(int, input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

queue = deque()
queue.append((x, 0))
result = []
visited = [0] * (n+1)
visited[x] = 1

while queue:
    city, count = queue.popleft()
    if count == k:
        result.append(city)
    for c in data[city]:
        if not visited[c]:
            queue.append((c, count+1))
            visited[c] = 1

if not result:
    print(-1)
else:
    result.sort()
    for r in result:
        print(r)