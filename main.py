import numpy as np
import sys
from validation import is_valid_board
from Board.Posibilities import Posibilities
from Board.Board import Board


# WIKIPEDIA
board = Board([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])
# EASY
# board = Board([
#     [7, 9, 4, 0, 8, 6, 3, 1, 0],
#     [1, 0, 2, 0, 7, 3, 5, 8, 9],
#     [0, 5, 0, 0, 9, 2, 0, 0, 0],
#     [0, 0, 0, 7, 5, 0, 1, 2, 0],
#     [0, 0, 7, 3, 0, 0, 0, 9, 6],
#     [0, 4, 0, 0, 1, 0, 0, 0, 0],
#     [4, 3, 0, 0, 0, 0, 0, 5, 1],
#     [0, 0, 0, 9, 0, 0, 6, 0, 0],
#     [6, 0, 1, 0, 3, 0, 0, 0, 0]
# ])
# EASY
# board = Board([
#     [0, 5, 0, 3, 1, 4, 0, 6, 0],
#     [8, 7, 0, 0, 0, 9, 4, 0, 3],
#     [6, 4, 3, 5, 0, 7, 1, 9, 2],
#     [0, 0, 7, 8, 0, 5, 2, 1, 0],
#     [4, 1, 0, 9, 0, 0, 0, 0, 0],
#     [0, 2, 5, 0, 6, 1, 9, 0, 7],
#     [7, 9, 0, 2, 5, 0, 8, 4, 0],
#     [0, 0, 4, 0, 9, 6, 0, 0, 5],
#     [0, 3, 0, 1, 0, 8, 6, 7, 0]
# ])
# MEDIUM
# board = Board([
#     [7, 6, 2, 0, 0, 0, 0, 0, 4],
#     [0, 8, 0, 0, 4, 0, 0, 0, 7],
#     [0, 5, 0, 0, 2, 8, 0, 1, 0],
#     [0, 0, 0, 6, 0, 4, 0, 3, 0],
#     [9, 0, 6, 0, 1, 2, 0, 4, 0],
#     [0, 2, 4, 0, 5, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 9, 0, 0, 0],
#     [0, 7, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 8, 4, 7, 3, 0, 6, 0]
# ])

if not is_valid_board(board):
    print('Board is not valid')
    sys.exit()

print(board)
print(f'Unsolved cells: {len(board)}\n')

posibilities = Posibilities(board.board)
posibilities.remove_duplicates_from_all_sections()
board.update_board(posibilities.matrix)

print(board)
print(f'Unsolved cells: {len(board)}')
