n, m = map(int, input().split())
road = []
for _ in range(m):
    a, b, c = map(int ,input().split())
    road.append((c, a, b))

road.sort()
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
last = 0
for c, a, b in road:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        last = c

print(result - last)
    