from collections import deque

n = int(input())
data = [[] for _ in range(n+1)]
time = [0]
degree = [0] * (n+1)
for i in range(1, n+1):
    d = list(map(int, input().split()))
    time.append(d[0])
    for j in d[1:-1]:
        data[j].append(i)
        degree[i] += 1

q = deque()

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

result = time[:]
while q:
    x = q.popleft()
    for i in data[x]:
        degree[i] -= 1
        result[i] = max(result[i], time[i] + result[x])
        if degree[i] == 0:
            q.append(i)

for i in range(1, n+1):
    print(result[i])