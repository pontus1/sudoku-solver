import numpy as np
import sys
from utils import is_valid_board, get_indexes_of_all_unsolved_cells, create_posibility_board, get_sections, get_unsolved_cells, get_cell_by_index, get_solved_numbers_in_section, get_solved_and_unsolved, subtract_imposible_numbers_from_section, solve_section, create_solved_board, get_unsolved_numbers_in_section, get_box_by_cell_index

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
# board = np.array([
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ])

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
# EASY SOLVED BY FIRST ALGORITM
board = np.array([
    [0, 5, 0, 3, 1, 4, 0, 6, 0],
    [8, 7, 0, 0, 0, 9, 4, 0, 3],
    [6, 4, 3, 5, 0, 7, 1, 9, 2],
    [0, 0, 7, 8, 0, 5, 2, 1, 0],
    [4, 1, 0, 9, 0, 0, 0, 0, 0],
    [0, 2, 5, 0, 6, 1, 9, 0, 7],
    [7, 9, 0, 2, 5, 0, 8, 4, 0],
    [0, 0, 4, 0, 9, 6, 0, 0, 5],
    [0, 3, 0, 1, 0, 8, 6, 7, 0]
])

# Validate board and exit if not valid
rows, columns, boxes = get_sections(board)
valid_board = is_valid_board(rows, columns, boxes)
if not valid_board:
    print('Board is not valid')
    sys.exit()

# Print amount of solved cells on board
total_number_of_cells = 81
unsolved_cells = len(get_indexes_of_all_unsolved_cells(board))
number_of_solved_cells = total_number_of_cells - unsolved_cells
print(f'Solved cells when starting: {number_of_solved_cells}\n')

# create posibility board (3d matrix)
posibility_board = create_posibility_board(board)


while True:
    unsolved_cells_before = get_unsolved_cells(posibility_board)
    # subtract solved numers from unsolved cells (replace with 0)
    # solve rows
    for row in range(9):
        solve_section(posibility_board[row:row+1, :, :].reshape(9, 9))
    # solve columns
    for column in range(9):
        solve_section(posibility_board[:, column:column+1, :].reshape(9, 9))
    # solve boxes TODO: figure out a loop
    solve_section(posibility_board[:3, :3, :].reshape(9, 9))
    solve_section(posibility_board[:3, 3:6, :].reshape(9, 9))
    solve_section(posibility_board[:3, 6:, :].reshape(9, 9))
    solve_section(posibility_board[3:6, :3, :].reshape(9, 9))
    solve_section(posibility_board[3:6, 3:6, :].reshape(9, 9))
    solve_section(posibility_board[3:6, 6:, :].reshape(9, 9))
    solve_section(posibility_board[6:, :3, :].reshape(9, 9))
    solve_section(posibility_board[6:, 3:6, :].reshape(9, 9))
    solve_section(posibility_board[6:, 6:, :].reshape(9, 9))

    unsolved_cells_after = get_unsolved_cells(posibility_board)
    number_of_solved_cells = total_number_of_cells - len(unsolved_cells_after)

    if len(unsolved_cells_before) == len(unsolved_cells_after):
        print(f'Solved cells when finished: {number_of_solved_cells}\n')
        break

board = create_solved_board(posibility_board)
print('Board:')
print(board)
print('\n\n')


rows, columns, boxes = get_sections(board)

# TODO: change to 9
for row_num in range(1):
    unsolved_numbers, unsolved_indexes = get_unsolved_numbers_in_section(
        rows[row_num])

    print(unsolved_numbers, unsolved_indexes)
    for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_indexes):
        box = get_box_by_cell_index(row_num, unsolved_index, board)

        if np.isin(unsolved_number, box):
            arr = posibility_board[row_num:row_num +
                                   1, unsolved_index:unsolved_index+1, :]
            arr[arr == unsolved_number] = 0

board = create_solved_board(posibility_board)
print('Board:')
print(board)
print('\n\n')
# row0 = posibility_board[:1, :, :].reshape(9, 9)  # row 0
# column0 = posibility_board[:, :1, :].reshape(9, 9)  # column 0
# box0 = posibility_board[:3, :3, :].reshape(9, 9) # box 0

print(posibility_board[2:3, :, :])

# TODO:
# get indexes of all unsolved cells
# for each unsolved cell
# 1 get row index and check row
# 2 get column index and check column
# 3 get box index and check box
# This is one iteration and it will keep iterating until length of unsolved cells is equal to prev length of unsolved cells

# a = np.delete(a, indices)
# boxes
# board[:3, :3] = 1  # box_0
# board[:3, 3:6] = 2  # box_1
# board[:3, 6:] = 3  # box_2

# board[3:6, :3] = 4  # box_3
# board[3:6, 3:6] = 5  # box_4
# board[3:6, 6:] = 6  # box_5

# board[6:, :3] = 7  # box_6
# board[6:, 3:6] = 8  # box_7
# board[6:, 6:] = 9  # box_8

# # rows
# row_0 = board[0]
# row_1 = board[1]
# row_2 = board[2]
# row_3 = board[3]
# row_4 = board[4]
# row_5 = board[5]
# row_6 = board[6]
# row_7 = board[7]
# row_8 = board[8]

# # columns
# column_0 = board[:, :1]
# column_1 = board[:, 1:2]
# column_2 = board[:, 2:3]
# column_3 = board[:, 3:4]
# column_4 = board[:, 4:5]
# column_5 = board[:, 5:6]
# column_6 = board[:, 6:7]
# column_7 = board[:, 7:8]
# column_8 = board[:, 8:]


# [
#     [0 0 3 0 0 0 0 0 9]
#     [0 0 0 0 0 0 0 8 0]
#     [0 0 3 0 0 6 0 0 9] 6 går att lösa
#     [0 0 0 0 0 0 7 0 0]
#     [0 0 0 0 5 0 0 0 0]
#     [0 0 0 4 0 0 0 0 9]
#     [1 0 0 0 0 0 0 0 0]
#     [0 2 0 0 0 0 0 0 0]
#     [0 0 3 4 0 0 0 0 0]
# ]
