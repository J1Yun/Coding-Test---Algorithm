n, m = map(int ,input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

command = list(map(int, input().split()))

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

parent = [0] * (m+1)

for i in range(1, m+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            union_parent(parent, i, j)

flag = True
prev = find_parent(parent, command[0])
for c in command:
    if prev != find_parent(parent, c):
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')
