def solution(N, stages):
    num = len(stages)
    data = [0] * (N+2)
    result = []
    for s in stages:
        data[s] += 1

    for i in range(1, N+1):
        if data[i]:
            result.append((i, data[i]/num ))
        else:
            result.append((i, 0))
        num -= data[i]

    result.sort(key = lambda x: (-x[1], x[0]))

    answer = []
    for r in result:
        answer.append(r[0])

    return answer
