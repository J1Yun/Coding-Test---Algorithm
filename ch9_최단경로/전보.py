import heapq
INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance[c] = 0

q = []
heapq.heappush(q, (0, c))
while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

count, result = 0, 0
for i in range(1, n+1):
    if 0 < distance[i] < INF:
        count += 1
        result = max(result, distance[i])

print(count, result)
