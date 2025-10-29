# Tic-Tac-Toe AI
This project implements a **simple rule-based (knowledge-based) AI** that plays the classic Tic-Tac-Toe game intelligently.

## How it works
The AI uses logical rules in this order of priority:
1. **Win if possible** - Complete three in a row.
2. **Block opponent** - Stop the opponent from winning.
3. **Take the center** - If available.
4. **Take a corner** - Prefer corners if free.
5. **Take a side** - Pick any remaining side.

## Function Definition
The AI is implemented as a single function called `play()`.

```python
def play(board):
    # board: list of 9 strings ('x', 'o', or '')
    # returns: integer from 0-8 representing the next move.
```
**Board Mapping:**
