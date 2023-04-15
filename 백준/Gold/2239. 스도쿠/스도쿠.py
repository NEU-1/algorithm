import sys

def is_possible(x, y, num, board):
    for i in range(9):
        if board[x][i] == num or board[i][y] == num:
            return False

    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[nx + i][ny + j] == num:
                return False

    return True

def solve(board):
    global is_finished
    if is_finished:
        return

    is_empty = False
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                is_empty = True
                x, y = i, j
                break
        if is_empty:
            break

    if not is_empty:
        is_finished = True
        for row in board:
            print("".join(map(str, row)))
        return

    for num in range(1, 10):
        if is_possible(x, y, num, board):
            board[x][y] = num
            solve(board)
            if not is_finished:
                board[x][y] = 0

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(9)]
is_finished = False
solve(board)
