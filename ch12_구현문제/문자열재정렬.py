s = input()
result = []
number = 0

for i in s:
    if i.isdigit():
        number += int(i)
    else:
        result.append(i)

result.sort()
if number:
    result.append(str(number))

print(''.join(result))
