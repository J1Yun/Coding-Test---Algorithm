n = int(input())
data = list(map(int, input().split()))

start, end = 0, n-1
result = -1
while start <= end:
    mid = (start + end) // 2
    if data[mid] == mid:
        result = data[mid]
        break
    elif data[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1

if result != -1:
    print(result)
else:
    print(-1)