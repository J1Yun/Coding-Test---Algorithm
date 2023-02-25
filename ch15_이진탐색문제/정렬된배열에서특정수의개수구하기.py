import bisect

n, x = map(int, input().split())
data = list(map(int,input().split()))

l = bisect.bisect_left(data, x)
r = bisect.bisect_right(data, x)

if r - l:
    print(r-l)
else:
    print(-1)