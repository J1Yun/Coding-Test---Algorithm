def rotate(matrix):
    return list(map(list, zip(*matrix[::-1])))

def check(matrix, n):
    for i in range(n, n*2):
        for j in range(n, n*2):
            if matrix[i][j] != 1:
                return False
    return True


def solution(key, lock):
    length = len(lock)
    key_length = len(key)
    data = [[0] * (length*3) for _ in range(length*3)]

    for i in range(length):
        for j in range(length):
            data[length+i][length+j] = lock[i][j]
            
    for _ in range(4):
        key = rotate(key)
        for i in range(length*2):
            for j in range(length*2):
                for k in range(key_length):
                    for l in range(key_length):
                        data[i+k][j+l] += key[k][l]
                
                if check(data, length):
                    return True

                for k in range(key_length):
                    for l in range(key_length):
                        data[i+k][j+l] -= key[k][l]

    return False