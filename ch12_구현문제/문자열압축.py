def solution(s):
    result = len(s)
        
    for i in range(1, len(s) // 2 + 1):
        data = []
        for j in range(0, len(s), i):
            data.append(s[j:j+i])

        count = 0
        string = ''
        for j in range(len(data)-1):
            if data[j] == data[j+1]:    
                count += 1
            else:
                if count > 0:
                    string += str(count+1) + data[j]
                else:
                    string += data[j]
                count = 0
        if count > 0:
            string += str(count+1) + data[-1]
        else:
            string += data[-1]
        
        result = min(result, len(string))

    return result