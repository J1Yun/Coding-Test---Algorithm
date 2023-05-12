from collections import deque

t = int(input())
answer = []
for _ in range(t):
    n = int(input())
    rank = list(map(int ,input().split()))
    data = [[False]*(n+1) for _ in range(n+1)]
    indegree = [0] * (n+1)

    for i in range(n):
        for j in range(i+1, n):
            data[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int ,input().split())
        if data[a][b]: 
            data[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            data[a][b] = True
            data[b][a] = False
            indegree[b] += 1
            indegree[a] -= 1

    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    isMany = False
    result = []
    while q:
        if len(q) > 1:
            isMany = True
            break

        x = q.popleft()
        result.append(x)

        for i in range(1, n+1):
            if data[x][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if len(result) != n:
        print('IMPOSSIBLE')
    elif isMany:
        print('?')
    else:
        for r in result:
            print(r, end=' ')