def safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(board, row, n):
    if row == n:
        print(board)
        return

    for col in range(n):
        if safe(board, row, col):
            board[row] = col
            solve(board, row + 1, n)

n = 5
board = [-1] * n
solve(board, 0, n)