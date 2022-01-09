import numpy as np
import sys
from validation import is_valid_board
from board_utils import get_indexes_of_all_unsolved_cells, create_posibility_matrix
from utils import update_board, remove_posibilities_1, remove_posibilities2

# board = np.array([
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ])
# WIKIPEDIA
board = np.array([
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

# MEDIUM
# board = np.array([
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
# EASY
# board = np.array([
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
# EASY - SOLVED BY FIRST ALGORITM
# board = np.array([
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

# Validate board and exit if not valid
if not is_valid_board(board):
    print('Board is not valid')
    sys.exit()

# Print amount of solved cells on board
total_number_of_cells = 81
unsolved_cells = len(get_indexes_of_all_unsolved_cells(board))
number_of_solved_cells = total_number_of_cells - unsolved_cells
print(
    f'Unsolved cells when starting: {len(get_indexes_of_all_unsolved_cells(board))}\n')

# # create posibility board (3d matrix)
posibility_board = create_posibility_matrix(board)

remove_posibilities_1(posibility_board)


board = update_board(posibility_board)
print('Board:')
print(board)
print('\n\n')

# TODO: kör tills det tar stopp
remove_posibilities2(board, posibility_board)
board = update_board(posibility_board)

print('Posibilities: ', np.count_nonzero(posibility_board))
board = update_board(posibility_board)
print('Board:')
print(board)
print('\n\n')


# row0 = posibility_board[:1, :, :].reshape(9, 9)  # row 0
# column0 = posibility_board[:, :1, :].reshape(9, 9)  # column 0
# box0 = posibility_board[:3, :3, :].reshape(9, 9) # box 0

# print(posibility_board[2:3, :, :])
