n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(len(data[i])):
        value = 0
        if j - 1 >= 0:
            value = max(value, data[i-1][j-1])
        if j < len(data[i-1]):
            value = max(value, data[i-1][j])

        data[i][j] = value + data[i][j]

print(max(data[-1]))