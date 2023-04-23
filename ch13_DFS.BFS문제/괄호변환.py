def check_correct(s):
    count = {'(': 0, ')': 0}
    flag = True

    for i in s:
        count[i] += 1
        if count['('] < count[')']:
            flag = False
            break

    return flag


def make_correct(u, v):
    temp = '(' + repeat(v) + ')'
    for i in range(1, len(u)-1):
        if u[i] == '(':
            temp += ')'
        else:
            temp += '('
    return temp


def repeat(s):
    if not s:
        return s

    count = {'(': 0, ')': 0}
    u, v = '', ''

    for i in range(len(s)):
        count[s[i]] += 1
            
        if count['('] == count[')']:
            u, v = s[:i+1], s[i+1:]
            break

    if check_correct(u):
        return u + repeat(v)
    else:
        return make_correct(u, v)
    

def solution(p):
    return repeat(p)