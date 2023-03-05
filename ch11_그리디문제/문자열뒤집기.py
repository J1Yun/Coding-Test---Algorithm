s = input()
count = {'0': 0, '1': 0}

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        count[s[i-1]] += 1
count[s[-1]] += 1

print(min(count.values()))