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
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

Example input:
```python
['','x','x','o','','','','','']
```
represents:
|   | X | X |
| O |   |   |
|   |   |   |

## Running the Code
Make sure you have Python 3.x installed.

Run the file directly:
```bash
python tictactoe_ai.py
```
Or use it inside another script:
```python
from tictactoe_ai import play
board = ['','x','x','o','','','','','']
move = play(board)
print("AI chooses: ", move)
```

## Author
**Stephanie Illo**
_Data Science and AI Enthusiast_

## Notes
* This is a **rule-based AI**, not a learning model.
* It shows how to design a simple **knowledge-based reasoning system** for games.
* Followed logical priority to make consistent and legal moves.
