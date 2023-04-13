from itertools import permutations

def solution(n, weak, dist):
    weaksize = len(weak)
    if weaksize == 1:
        return 1
    perm_friends = list(permutations(dist, len(dist)))
    min_val = 1e9
    
    for start in range(weaksize):
        for pf in perm_friends:
            count = 1
            now = start
            for i in range(1, weaksize):
                next = (start + i) % weaksize
                temp = weak[next] - weak[now] if weak[next] >= weak[now] else n - weak[now] + weak[next]
                if temp > pf[count-1]:
                    now = next
                    count += 1
                    if count > len(dist):
                        break
            if count <= len(dist):
                min_val = min(min_val, count)

    if min_val == 1e9:
        return -1
    else:
        return min_val
