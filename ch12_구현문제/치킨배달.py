from itertools import combinations

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i, j))
        elif data[i][j] == 1:
            house.append((i, j))

result = 1e9
for d in list(combinations(chicken, m)):
    summary = 0
    for x1, y1 in house:
        min_dist = 1e9
        for x2, y2 in d:
            min_dist = min(abs(x1-x2) + abs(y1-y2), min_dist)
        summary += min_dist
    result = min(result, summary)

print(result)
