n, m = map(int, input().split())
d = [10001] * (m+1)
coin = []
for i in range(n):
    coin.append(int(input()))
    
d[0] = 0
for i in coin:
    for j in range (i, m+1):
        if d[j-i] != 10001:
            d[j] = min(d[j], d[j-i] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])



# n, m = map(int, input().split())
# d = [10001] * (m+1)
# coin = []
# for i in range(n):
#     coin.append(int(input()))

# d[0] = 0

# for i in range(1, m+1):
#     for c in coin:
#         t = i - c
#         if t >= 0 and d[t] != 10001:
#             d[i] = min(d[i], d[t] + 1)

# if d[m] == 10001:
#     print(-1)
# else:
#     print(d[m])
