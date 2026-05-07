from tictactoe import initial_state, actions

X = "X"
O = "O"
EMPTY = None

board=[[X, EMPTY, X],
       [EMPTY, X, O],
       [X, EMPTY, O]]

print(actions(board))