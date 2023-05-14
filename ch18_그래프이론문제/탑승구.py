# union-find 풀이 복습

g = int(input())
p = int(input())

indegree = [0] * (g+1)
for _ in range(p):
    x = int(input())
    for i in range(1, x+1):
        indegree[i] += 1

m = 0
result = 0
for i in range(g,0,-1):
    amount = indegree[i] - m
    if amount >= 1:
        result += 1
        m += amount
print(result)