def play(board):
    """
    Rule-based AI for Tic-Tac-Toe.
    Receives: board (list of 9 strings: 'x', 'o', or '').
    Returns: index (0-8) for next move based on simple rules.
    The first player is always 'x'
    """

    # Define players based on current turn
    x_count = board.count('x')
    o_count = board.count('o')
    turn = 'x' if x_count == o_count else 'o'

    # All winning combinations (using indices)
    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    # Rule 1: If we can win this turn, take it
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(turn) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # Rule 2: Block opponent if they can win next turn
    opponent = 'o' if turn == 'x' else 'x'
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

    # Rule 3: Take the center if free
    if board[4] == '':
        return 4

    # Rule 4: Take a corner if available
    corners = [0, 2, 6, 8]
    for i in corners:
        if board[i] == '':
            return i

    # Rule 5: Take any remaining side
    sides = [1, 3, 5, 7]
    for i in sides:
        if board[i] == '':
            return i
