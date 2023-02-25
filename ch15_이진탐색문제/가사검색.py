import bisect

def solution(words, queries):
    reversed_words, forward_words = [], []
    for w in words:
        forward_words.append((len(w), w))
    for w in words:
        reversed_words.append((len(w), w[::-1]))

    forward_words.sort()
    reversed_words.sort()

    result = []
    for q in queries:
        
        length = len(q)
        if q[0] == '?':
            l = bisect.bisect_left(reversed_words, (length, q[::-1]))
            r = bisect.bisect_right(reversed_words, (length, q.replace('?', '~')[::-1]))
        else:
            l = bisect.bisect_left(forward_words, (length, q))
            r = bisect.bisect_right(forward_words, (length, q.replace('?', '~')))

        result.append(r - l)

    return result
