s = input()
result = 0

for num in s:
    num = int(num)
    if num == 1 or num == 0 or result == 1 or result == 0:
        result += num
    else:
        result *= num
    
print(result)