from copy import deepcopy

def move(board, direction):
    if direction == 0:  # 상
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[j][i]:
                    temp = board[j][i]
                    board[j][i] = 0
                    if board[idx][i] == temp:
                        board[idx][i] *= 2
                        idx += 1
                    else:
                        if board[idx][i]:
                            idx += 1
                        board[idx][i] = temp
    elif direction == 1:  # 하
        for i in range(N):
            idx = N-1
            for j in range(N-2, -1, -1):
                if board[j][i]:
                    temp = board[j][i]
                    board[j][i] = 0
                    if board[idx][i] == temp:
                        board[idx][i] *= 2
                        idx -= 1
                    else:
                        if board[idx][i]:
                            idx -= 1
                        board[idx][i] = temp
    elif direction == 2:  # 좌
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == temp:
                        board[i][idx] *= 2
                        idx += 1
                    else:
                        if board[i][idx]:
                            idx += 1
                        board[i][idx] = temp
    else:  # 우
        for i in range(N):
            idx = N-1
            for j in range(N-2, -1, -1):
                if board[i][j]:
                    temp = board[i][j]
                    board[i][j] = 0
                    if board[i][idx] == temp:
                        board[i][idx] *= 2
                        idx -= 1
                    else:
                        if board[i][idx]:
                            idx -= 1
                        board[i][idx] = temp

def dfs(board, cnt):
    if cnt == 5:
        return max(map(max, board))
    
    max_value = 0
    for d in range(4):
        new_board = deepcopy(board)
        move(new_board, d)
        max_value = max(max_value, dfs(new_board, cnt+1))
        
    return max_value

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(dfs(board, 0))
