"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    n_X = 0
    n_O = 0
    if board == initial_state():
        return "X"
    for l in board:
        for s in l:
            if s == X:
                n_X = n_X + 1
            elif s == O:
                n_O = n_O + 1
    if n_X == n_O:
        return "X"
    else:
        return "O"
        

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, l in enumerate(board):
        for j, s in enumerate(l):
            if s == None:
                actions.add((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board=deepcopy(board)
    if player(board) == "X":
        copy_board[action[0]][action[1]] = "X"
    else:
        copy_board[action[0]][action[1]] = "O"
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal win conditions for player X.
    try:    
        if board[0][0]+board[0][1]+board[0][2] == "XXX":
            return X
    except TypeError:
        pass
    try:    
        if board[1][0]+board[1][1]+board[1][2] == "XXX":
            return X
    except TypeError:
        pass
    try:    
        if board[2][0]+board[2][1]+board[2][2] == "XXX":
            return X
    except TypeError:
        pass
    
    # Horizontal win conditions for player O
    try:    
        if board[0][0]+board[0][1]+board[0][2] == "OOO":
            return O
    except TypeError:
        pass
    try:    
        if board[1][0]+board[1][1]+board[1][2] == "OOO":
            return O
    except TypeError:
        pass
    try:    
        if board[2][0]+board[2][1]+board[2][2] == "OOO":
            return O
    except TypeError:
        pass
    
    # Vertical win conditions for player X.
    try:    
        if board[0][0]+board[1][0]+board[2][0] == "XXX":
            return X
    except TypeError:
        pass
    try:    
        if board[0][1]+board[1][1]+board[2][1] == "XXX":
            return X
    except TypeError:
        pass
    try:    
        if board[0][2]+board[1][2]+board[2][2] == "XXX":
            return X
    except TypeError:
        pass
    
    # Vertical win conditions for player O.
    try:    
        if board[0][0]+board[1][0]+board[2][0] == "OOO":
            return O
    except TypeError:
        pass
    try:    
        if board[0][1]+board[1][1]+board[2][1] == "OOO":
            return O
    except TypeError:
        pass
    try:    
        if board[0][2]+board[1][2]+board[2][2] == "OOO":
            return O
    except TypeError:
        pass
    
    # Diagonal win conditions for player X.
    try:    
        if board[0][0]+board[1][1]+board[2][2] == "XXX":
            return X
    except TypeError:
        pass
    try:    
        if board[0][2]+board[1][1]+board[2][0] == "XXX":
            return X
    except TypeError:
        pass

    # Diagonal win conditions for player X.
    try:    
        if board[0][0]+board[1][1]+board[2][2] == "OOO":
            return O
    except TypeError:
        pass
    try:    
        if board[0][2]+board[1][1]+board[2][0] == "OOO":
            return O
    except TypeError:
        pass
    
    # No winner or a draw.
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
