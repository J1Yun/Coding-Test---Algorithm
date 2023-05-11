n, m = map(int ,input().split())

data = []
total = 0
for _ in range(m):
    x, y, z = map(int ,input().split())
    data.append((z, x, y))
    total += z

data.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

result = 0
for z, x, y in data:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += z

print(total - result)