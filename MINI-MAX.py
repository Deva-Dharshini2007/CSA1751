import math

# Sample evaluation function (for demonstration)
def evaluate(board):
    """
    Returns +10 if 'X' wins, -10 if 'O' wins, 0 otherwise
    board : list of lists 3x3
    """
    # Rows
    for row in board:
        if row.count('X') == 3:
            return 10
        if row.count('O') == 3:
            return -10
    # Columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count('X') == 3:
            return 10
        if [board[row][col] for row in range(3)].count('O') == 3:
            return -10
    # Diagonals
    if [board[i][i] for i in range(3)].count('X') == 3 or [board[i][2-i] for i in range(3)].count('X') == 3:
        return 10
    if [board[i][i] for i in range(3)].count('O') == 3 or [board[i][2-i] for i in range(3)].count('O') == 3:
        return -10
    return 0

# Check if moves left
def is_moves_left(board):
    for row in board:
        if '-' in row:
            return True
    return False

# Minimax function
def minimax(board, depth, is_max):
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
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = '-'
        return best
    else:  # Minimizer 'O'
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = '-'
        return best

# Find the best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
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
