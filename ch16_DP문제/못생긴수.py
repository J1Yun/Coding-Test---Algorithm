n = int(input())

count = 1
num = 2
dp = [0] * 2000
dp[1] = 1
while count < n:
    if num % 2 == 0:
        dp[num] = dp[num//2]
    elif num % 3 == 0:
        dp[num] = dp[num//3]
    elif num % 5 == 0:
        dp[num] = dp[num//5]
    if dp[num]:
        count += 1
    num += 1

print(num-1)