n, m = map(int, input().split())
result = []
parents = [0] * (n+1)

for i in range(1, n+1):
    parents[i]= i

def find_parent(parents, x):
    if parents[x] != x:
        parents[x] = find_parent(parents, parents[x])
    return parents[x]

def union_parent(parents, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

for _ in range(m):
    t, a, b = map(int, input().split())
    if t:
        if find_parent(parents, a) == find_parent(parents, b):
            result.append('YES')
        else:
            result.append('NO')
    else:
        union_parent(parents, a, b)

for r in result:
    print(r)