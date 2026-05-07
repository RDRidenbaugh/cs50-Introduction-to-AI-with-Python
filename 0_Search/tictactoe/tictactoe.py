"""
Tic Tac Toe Player
"""

import math

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


def parse_XO(board):
    """
    Identifies the the number of X's and O's already played.
    """
    nX = 0
    nO = 0
    for l in board:
        for s in l:
            if s == X:
                nX = nX + 1
            elif s == O:
                nO = nO + 1
    if nX == nO:
        return "X"
    else:
        return "O"


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return "X"
    else:
        if parse_XO(board) == "X":
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
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


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
