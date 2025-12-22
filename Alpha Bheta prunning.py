import math

# Sample evaluation function
def evaluate(board):
    # +10 for 'X' win, -10 for 'O' win, 0 otherwise
    for row in board:
        if row.count('X') == 3:
            return 10
        if row.count('O') == 3:
            return -10
    for col in range(3):
        if [board[row][col] for row in range(3)].count('X') == 3:
            return 10
        if [board[row][col] for row in range(3)].count('O') == 3:
            return -10
    if [board[i][i] for i in range(3)].count('X') == 3 or [board[i][2-i] for i in range(3)].count('X') == 3:
        return 10
    if [board[i][i] for i in range(3)].count('O') == 3 or [board[i][2-i] for i in range(3)].count('O') == 3:
        return -10
    return 0

def is_moves_left(board):
    for row in board:
        if '-' in row:
            return True
    return False

# Alpha-Beta pruning function
def alphabeta(board, depth, alpha, beta, is_max):
    score = evaluate(board)

    # Terminal states
    if score == 10 or score == -10:
        return score
    if not is_moves_left(board):
        return 0

    if is_max:  # Maximizer 'X'
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = max(best, alphabeta(board, depth+1, alpha, beta, False))
                    board[i][j] = '-'
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break  # Beta cut-off
        return best
    else:  # Minimizer 'O'
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, alphabeta(board, depth+1, alpha, beta, True))
                    board[i][j] = '-'
                    beta = min(beta, best)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return best

# Find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                move_val = alphabeta(board, 0, -math.inf, math.inf, False)
                board[i][j] = '-'
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
    return best_move

# Example board
board = [
    ['X', 'O', 'X'],
    ['O', 'O', '-'],
    ['-', '-', 'X']
]

best_move = find_best_move(board)
print("Best move for X is:", best_move)
