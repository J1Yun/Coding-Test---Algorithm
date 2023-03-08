n, m = map(int, input().split())
data = list(map(int, input().split()))

balls = [0] * (m+1)
for d in data:
    balls[d] += 1

result = 0
for i in balls:
    n -= i
    result += i * n

print(result)