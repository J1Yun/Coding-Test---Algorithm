n = int(input())
data = []
for i in range(n):
    x, y, z = map(int ,input().split())
    data.append((i, x, y, z))

edges = []
for i in range(1, 4):
    data.sort(key=lambda x : x[i])
    for j in range(n-1):
        edges.append((abs(data[j][i]-data[j+1][i]), data[j][0], data[j+1][0]))
        
edges.sort()

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

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
for cost, x, y in edges:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result += cost

print(result)
