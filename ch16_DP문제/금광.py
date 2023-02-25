t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    length = len(data)
    dp = [0] * length

    for i in range(0, length, m):
        dp[i] = data[i]

    for i in range(1, m):
        for j in range(n):
            value = 0

            if (j-1) * m + i - 1 >= 0:
                value = max(value, dp[(j-1) * m + i - 1])
            if j * m + i - 1 >= 0:
                value = max(value, dp[j * m + i - 1])
            if (j+1) * m + i - 1 < length:
                value = max(value, dp[(j+1) * m + i - 1])

            dp[j * m + i] = data[j * m + i] + value

    max_val = 0
    for i in range(m-1, length, m):
        max_val = max(max_val, dp[i])

    result.append(max_val)

for r in result:
    print(r)