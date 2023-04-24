from collections import deque

def turn(lx, ly, rx, ry, d, board):

    n = len(board)
    array = []
    dx, dy = {0: [1, -1], 1: [0, 0]}, {0: [0, 0], 1: [1, -1]}
    
    for i in range(2):
        lnx, lny, rnx, rny = lx + dx[d][i], ly + dy[d][i], rx + dx[d][i], ry + dy[d][i]
        if lnx < 0 or lnx >= n or lny < 0 or lny >= n or rnx < 0 or rnx >= n or rny < 0 or rny >= n or board[lnx][lny] or board[rnx][rny]:
            continue
        
        array.append((lx, ly, lnx, lny))
        array.append((rx, ry, rnx, rny))
    
    return array



def solution(board):

    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
    n = len(board)
    visited = [{(0, 0), (0, 1)}]

    queue = deque()
    queue.append((0, 0, 0, 1, 0, 0))

    while queue:
        left_x, left_y, right_x, right_y, d, t = queue.popleft()
        if (left_x, left_y) == (n-1, n-1) or (right_x, right_y) == (n-1, n-1):
                return t

        for i in range(4):
            left_nx, left_ny, right_nx, right_ny = left_x + dx[i], left_y + dy[i], right_x + dx[i], right_y + dy[i]
            if left_nx < 0 or left_nx >= n or left_ny < 0 or left_ny >= n or right_nx < 0 or right_nx >= n or right_ny < 0 or right_ny >= n or board[left_nx][left_ny] or board[right_nx][right_ny] or {(left_nx, left_ny), (right_nx, right_ny)} in visited:
                continue

            visited.append({(left_nx, left_ny), (right_nx, right_ny)})

            if left_nx <= right_nx or left_ny <= right_ny:
                queue.append((left_nx, left_ny, right_nx, right_ny, d, t+1))
            else:
                queue.append((right_nx, right_ny, left_nx, left_ny, d, t+1))

        for left_nx, left_ny, right_nx, right_ny in turn(left_x, left_y, right_x, right_y, d, board):
            if {(left_nx, left_ny), (right_nx, right_ny)} not in visited:
                queue.append((left_nx, left_ny, right_nx, right_ny, (d+1)%2, t+1))
                visited.append({(left_nx, left_ny), (right_nx, right_ny)})

