# Rule-based Tic Tac Toe AI
# Follows simple priorities: win > Block > Center > Corner > Any

import random

def play(board):
    """
    Receives: board (list of 9 strings: 'x', 'o', or '')
    Returns: index (0-8) for next move based on simple rules
    """

    # Define players based on current turn
    x_count = board.count('x')
    o_count = board.count('o')
    ai = 'o' if x_count > o_count else 'x' # it is o's turn if x has played more
    opponent = 'x' if ai == 'o' else 'o'

    # All winning lines (using indices)
    WINS = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    # Helper to find winning moves
    def find_winning_move(symbol):
        for win in WINS:
            symbols = [board[i] for i in win]
            if symbols.count(symbol) == 2 and symbols.count('') == 1:
                return win[symbols.index('')]
        return None

    # Rule 1: Win if possible
    move = find_winning_move(ai)
    if move is not None:
        return move

    # Rule 2: Block opponent
    move = find_winning_move(opponent)
    if move is not None:
        return move

    # Rule 3: Take center
    if board[4] == '':
        return 4

    # Rule 4: Take a corner
    corners = [0,2,6,8]
    random.shuffle(corners)
    for i in corners:
        if board[i] == '':
            return i

    # Rule 5: Take any remaining empty cell
    empty_cell = [i for i, v in enumerate(board) if v == '']
    if empty_cell:
        return random.choice(empty_cell)

    # No move possible (i.e board is full)
    return -1
