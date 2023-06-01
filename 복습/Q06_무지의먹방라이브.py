import heapq

def solution(food_times, k):
    queue = []

    n = len(food_times)
    if sum(food_times) <= k:
        return -1

    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i], i+1))

    h = 0
    while 1:
        if n * (queue[0][0]-h) <= k:
            food, _ = heapq.heappop(queue)
            k -= n * (food - h)
            n -= 1
            h = food
        else:
            break

    queue.sort(key = lambda x : x[1])
    return queue[k % n][1]
