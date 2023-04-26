n = int(input())
data = list(map(int, input().split()))
operation = list(map(int, input().split()))

def dfs(add, sub, mul, div, num, idx):
    global min_val, max_val

    if idx == n:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
        return
    if add:
        dfs(add-1, sub, mul, div, num + data[idx], idx+1)
    if sub:
        dfs(add, sub-1, mul, div, num - data[idx], idx+1)
    if mul:
        dfs(add, sub, mul-1, div, num * data[idx], idx+1)
    if div:
        dfs(add, sub, mul, div-1, int(num / data[idx]), idx+1)

min_val, max_val = 1e9, -1e9
dfs(operation[0], operation[1], operation[2], operation[3], data[0], 1)

print(max_val)
print(min_val)