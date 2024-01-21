import math
import copy

# Constants
X = "X"
O = "O"
EMPTY = None

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    return set((i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY)

def result(board, action):
    if action not in actions(board):
        raise Exception("Invalid action.")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    lines = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
             [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
             [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for line in lines:
        values = [board[i][j] for i, j in line]
        if values == [X, X, X]:
            return X
        elif values == [O, O, O]:
            return O
    return None

def terminal(board):
    return winner(board) is not None or not actions(board)

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        value = -math.inf
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value:
                value = new_value
                best_action = action
    else:
        value = math.inf
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value:
                value = new_value
                best_action = action
    return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value





