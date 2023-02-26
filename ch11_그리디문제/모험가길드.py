n = int(input())
data = list(map(int, input().split()))

data.sort()
group = 0
result = 0

for d in data:
    group += 1
    if group >= d:
        result += 1
        group == 0

print(result)