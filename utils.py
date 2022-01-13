import numpy as np

# def remove_posibilities2(board, posibility_board):
#     rows, columns, boxes = board.get_sections()

#     print('Posibilities: ', np.count_nonzero(posibility_board))
#     # remove posibilities from rows
#     for row_index in range(9):
#         unsolved_numbers, unsolved_column_indexes = board.get_unsolved_in_section(
#             rows[row_index])

#         for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_column_indexes):
#             box = board.get_box_by_row_and_col(row_index, unsolved_index)
#             column = board.get_column(unsolved_index)

#             if np.isin(unsolved_number, box) or np.isin(unsolved_number, column):
#                 arr = posibility_board[row_index:row_index +
#                                        1, unsolved_index:unsolved_index+1, :]
#                 arr[arr == unsolved_number] = 0

#     print('Posibilities: ', np.count_nonzero(posibility_board))
#     board.update_board(posibility_board)

#     # remove posibilities from columns
#     for column_index in range(9):
#         unsolved_numbers, unsolved_row_indexes = board.get_unsolved_in_section(
#             columns[column_index])

#         for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_row_indexes):
#             row = board[unsolved_index:unsolved_index+1]
#             box = board.get_box_by_row_and_col(column_index, unsolved_index)

#             if np.isin(unsolved_number, row) or np.isin(unsolved_number, box):
#                 arr = posibility_board[unsolved_index:unsolved_index +
#                                        1, unsolved_index:unsolved_index+1, :]
#                 arr[arr == unsolved_number] = 0

# remove posibilities from boxes
# for box_index in range(1):
#     # print(boxes[box_index])
#     unsolved_numbers, unsolved_indexes = get_unsolved_in_section(
#         boxes[box_index])
