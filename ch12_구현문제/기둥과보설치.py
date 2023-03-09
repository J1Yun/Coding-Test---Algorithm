def check(result):
    for x, y, a in result:
        if a == 1:
            if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
                continue
            else:
                return False
        else:
            if y == 0 or [x, y, 1] in result or [x-1, y, 1] in result or [x, y-1, 0] in result:
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
    answer.sort()
    return answer