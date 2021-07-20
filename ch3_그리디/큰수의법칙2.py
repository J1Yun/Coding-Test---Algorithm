n, m, k = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
a = num[n-1]
b = num[n-2]

result = (k*a+b) * (m//(k+1)) + a * (m%(k+1))
print(result)