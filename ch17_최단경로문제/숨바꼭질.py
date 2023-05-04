import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = []
heapq.heappush(q, (0, 1))
distance = [int(1e9)] * (n+1)
distance[1] = 0

while q:
    dist, x = heapq.heappop(q)
    if distance[x] < dist:
        continue
    for i in graph[x]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

max_val, max_idx = 0, 0
for i in range(2, n+1):
    if max_val < distance[i]:
        max_val, max_idx = distance[i], i
count = distance.count(max_val)

print(max_idx, max_val, count)
