n = input()
length = len(n)
summary1, summary2 = 0, 0

for i in range(length//2):
    summary1 += int(n[i])

for i in range(length//2, length):
    summary2 += int(n[i])

if summary1 == summary2:
    print('LUCKY')
else:
    print('READY')
