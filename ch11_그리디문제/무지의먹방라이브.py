import heapq

def solution(food_times, k):
    queue = []
    n = len(food_times)

    if sum(food_times) <= k:
        return -1

    for i in range(n):
        heapq.heappush(queue, (food_times[i], i+1))

    s, h = 0, 0
    while 1:
        if s + (queue[0][0] - h) * n > k:
            break
        temp = heapq.heappop(queue)[0]
        s += (temp - h) * n
        n -= 1
        h = temp

    queue.sort(key = lambda x : x[1])
    return queue[(k-s)%n][1]

