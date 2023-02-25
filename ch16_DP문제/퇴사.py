n =  int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
data.append([0, 0])
result = 0
for i in range(n-1, -1, -1):
    t = data[i][0]
    if i + t > n:
        data[i][1] = result
        continue
    data[i][1] = max(data[i + t][1] + data[i][1], result)
    result = data[i][1]

print(result)
