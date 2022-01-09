import numpy as np
import board_utils


# -------------------- #
# 3D POSIBILITY MATRIX #
# -------------------- #


def get_unsolved_cells(posibility_matrix: np.ndarray) -> np.ndarray:
    """
        Get an array of indexes of all unsolved cells in posibility matrix
        where each index is represented by [row index, column index]
        e.g. [[0 0][0 4][3 2][3 8]]

        Parameters
        ----------
        posibility_matrix: ndarray
            3d matrix of posibilities

        Returns
        -------
        ndarray: 2d array representing all unsolved cell indexes
    """
    unsolved_indexes = []
    for i in range(9):
        for j in range(9):
            non_zeros = np.count_nonzero(posibility_matrix[i:i+1, j:j+1])
            if non_zeros != 1:
                unsolved_indexes.append([i, j])
    return np.array(unsolved_indexes)


def get_solved_and_unsolved(cells):
    solved_numbers = []
    solved_indexes = []

    # get solved numbers
    # get solved indexes
    for i in range(9):
        non_zeros = np.count_nonzero(cells[0][i])
        if non_zeros == 1:
            solved_index = np.nonzero(cells[0][i])
            solved_numbers.append(cells[0][i][solved_index])
            solved_indexes.append(i)

    # get unsolved numbers
    all_numbers = np.arange(1, 10)
    indices = np.argwhere(np.isin(all_numbers, solved_numbers))
    unsolved_numbers = np.delete(all_numbers, indices)
    # get unsolved indexes
    all_indexes = np.arange(9)
    indices = np.argwhere(np.isin(all_indexes, solved_indexes))
    unsolved_indexes = np.delete(all_indexes, indices)

    # parse to np-arrays
    solved_numbers = np.array(solved_numbers).flatten()
    unsolved_numbers = np.array(unsolved_numbers)

    return (solved_numbers, unsolved_indexes)


def subtract_imposible_numbers_from_section(cells, unsolved_indexes, solved_numbers):
    for i in unsolved_indexes:
        for j in solved_numbers:
            cells[i][j-1] = 0
    return cells


def solve_section(section):
    solved_numbers, unsolved_indexes = get_solved_and_unsolved([section])
    updated_section = subtract_imposible_numbers_from_section(
        section, unsolved_indexes, solved_numbers)
    return updated_section


def update_board(posibility_matrix):
    board = []
    for idx in range(9):
        row = []
        for cell in posibility_matrix[idx:idx+1, :, :].reshape(9, 9):
            if np.count_nonzero(cell) == 1:
                # extract solved number and add to row
                row.append(cell[np.nonzero(cell)[0].tolist()[0]])
            else:
                # append 0 (since it's npt solved)
                row.append(0)
        board.append(row)
    return np.array(board)


def get_cell_by_index(posibility_matrix, cell):
    return posibility_matrix[cell[0]:cell[0]+1, cell[1]:cell[1]+1]


def get_solved_numbers_in_section(cells):
    """
        Get array of solved numbers in section (row, column, box)

        :param cells: a section of posibility board
        :return:      a flat array of solved numbers in section
    """
    temp_list = []
    for i in range(9):
        non_zeros = np.count_nonzero(cells[0][i])
        if non_zeros == 1:
            index_of_solved_value = np.nonzero(cells[0][i])
            temp_list.append(cells[0][i][index_of_solved_value])

    temp_list = np.array(temp_list).flatten()
    return temp_list


def remove_posibilities_1(posibility_matrix):
    """
        Remove solved numbers from each cell in a section. If e.g. the number 5 is solved in a row -
        all fives will be replaced by zeros on that row giving each cell less posibilities. This is
        repeated for all 9 rows, all 9 columns and all 9 boxes
        [
            [1 2 3 4 5 6 7 8 9]
            [1 2 3 4 5 6 7 8 9]
            [1 2 3 4 5 6 7 8 9]
            [1 2 3 4 5 6 7 8 9]
            [1 2 3 4 5 6 7 8 9]
            [0 0 0 0 5 0 0 0 0]
            [1 2 3 4 5 6 7 8 9]
            [1 2 3 4 5 6 7 8 9]
            [1 2 3 4 5 6 7 8 9]
        ]
        ->
        [
            [1 2 3 4 0 6 7 8 9]
            [1 2 3 4 0 6 7 8 9]
            [1 2 3 4 0 6 7 8 9]
            [1 2 3 4 0 6 7 8 9]
            [1 2 3 4 0 6 7 8 9]
            [0 0 0 0 5 0 0 0 0]
            [1 2 3 4 0 6 7 8 9]
            [1 2 3 4 0 6 7 8 9]
            [1 2 3 4 0 6 7 8 9]
        ]
    """

    while True:
        unsolved_cells_before = get_unsolved_cells(posibility_matrix)
        # subtract solved numers from unsolved cells (replace with 0)
        # solve rows
        for row in range(9):
            solve_section(posibility_matrix[row:row+1, :, :].reshape(9, 9))
        # solve columns
        for column in range(9):
            solve_section(
                posibility_matrix[:, column:column+1, :].reshape(9, 9))
        # solve boxes TODO: figure out a loop
        solve_section(posibility_matrix[:3, :3, :].reshape(9, 9))
        solve_section(posibility_matrix[:3, 3:6, :].reshape(9, 9))
        solve_section(posibility_matrix[:3, 6:, :].reshape(9, 9))
        solve_section(posibility_matrix[3:6, :3, :].reshape(9, 9))
        solve_section(posibility_matrix[3:6, 3:6, :].reshape(9, 9))
        solve_section(posibility_matrix[3:6, 6:, :].reshape(9, 9))
        solve_section(posibility_matrix[6:, :3, :].reshape(9, 9))
        solve_section(posibility_matrix[6:, 3:6, :].reshape(9, 9))
        solve_section(posibility_matrix[6:, 6:, :].reshape(9, 9))

        unsolved_cells_after = get_unsolved_cells(posibility_matrix)

        if len(unsolved_cells_before) == len(unsolved_cells_after):
            print(
                f'Unsolved cells when finished: {len(unsolved_cells_after)}\n')
            break


def remove_posibilities2(board, posibility_board):
    rows, columns, boxes = board_utils.get_sections(board)

    print('Posibilities: ', np.count_nonzero(posibility_board))
    # remove posibilities from rows
    for row_index in range(9):
        unsolved_numbers, unsolved_column_indexes = board_utils.get_unsolved_in_section(
            rows[row_index])

        for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_column_indexes):
            box = board_utils.get_box_by_cell_indexes(
                row_index, unsolved_index, board)
            column = board_utils.get_column_by_index(unsolved_index, board)

            if np.isin(unsolved_number, box) or np.isin(unsolved_number, column):
                arr = posibility_board[row_index:row_index +
                                       1, unsolved_index:unsolved_index+1, :]
                arr[arr == unsolved_number] = 0

    print('Posibilities: ', np.count_nonzero(posibility_board))
    board = update_board(posibility_board)

    # remove posibilities from columns
    for column_index in range(9):
        unsolved_numbers, unsolved_row_indexes = board_utils.get_unsolved_in_section(
            columns[column_index])

        for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_row_indexes):
            row = board[unsolved_index:unsolved_index+1]
            box = board_utils.get_box_by_cell_indexes(
                column_index, unsolved_index, board)

            if np.isin(unsolved_number, row) or np.isin(unsolved_number, box):
                arr = posibility_board[unsolved_index:unsolved_index +
                                       1, unsolved_index:unsolved_index+1, :]
                arr[arr == unsolved_number] = 0

    # remove posibilities from boxes
    # for box_index in range(1):
    #     # print(boxes[box_index])
    #     unsolved_numbers, unsolved_indexes = get_unsolved_in_section(
    #         boxes[box_index])
