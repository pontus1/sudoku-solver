import numpy as np
from section_type import Section


# -------------------- #
# 3D POSIBILITY MATRIX #
# -------------------- #

def get_posibility_section(type: Section, idx: int, posibility_matrix: np.ndarray) -> np.ndarray:
    """
        Get a 2d array of a posibility section, where each row is representing a cell and each element represents a posibility.

        Parameters
        ----------
        section: Section (Enum)
            one of 'row' | 'column' | 'box'

        idx: int
            index of section (0-8)

        Returns
        -------
        ndarray: 2d array of all posibilities in a section
    """
    if type == Section.Row:
        return posibility_matrix[idx:idx+1, :, :].reshape(9, 9)
    if type == Section.Column:
        return posibility_matrix[:, idx:idx+1, :].reshape(9, 9)
    if type == Section.Box:
        if idx == 0:
            return posibility_matrix[:3, :3, :].reshape(9, 9)
        if idx == 1:
            return posibility_matrix[:3, 3:6, :].reshape(9, 9)
        if idx == 2:
            return posibility_matrix[:3, 6:, :].reshape(9, 9)
        if idx == 3:
            return posibility_matrix[3:6, :3, :].reshape(9, 9)
        if idx == 4:
            return posibility_matrix[3:6, 3:6, :].reshape(9, 9)
        if idx == 5:
            return posibility_matrix[3:6, 6:, :].reshape(9, 9)
        if idx == 6:
            return posibility_matrix[6:, :3, :].reshape(9, 9)
        if idx == 7:
            return posibility_matrix[6:, 3:6, :].reshape(9, 9)
        if idx == 8:
            return posibility_matrix[6:, 6:, :].reshape(9, 9)

    return np.array([])


def get_solved_and_unsolved_in_section(section: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
        Get a tuple of solved numbers as 1d array and unsolved indexes as 1d array from a section.
        Solved numbers contains all numbers that are solved in passed section.
        Unsolved indexes contains all indexes of unsolved numbers in passed section

        Parameters
        ----------
        section: ndarray
            section to get numbers and indexes from

        Returns
        -------
        tuple:  ndarray of all solved numbers in section, ndarray of all unsolved indexes in section
    """
    solved_numbers = []
    solved_indexes = []

    # get solved numbers
    # get solved indexes
    for i in range(9):
        non_zeros = np.count_nonzero(section[i])
        if non_zeros == 1:
            solved_index = np.nonzero(section[i])
            solved_numbers.append(section[i][solved_index])
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
    unsolved_numbers = np.array(unsolved_numbers)

    return (np.array(solved_numbers).flatten(), unsolved_indexes)


def get_unsolved_cell_indexes(posibility_matrix: np.ndarray) -> np.ndarray:
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


def remove_posibilities_from_section(section):
    solved_numbers, unsolved_indexes = get_solved_and_unsolved_in_section(
        section)
    for i in unsolved_indexes:
        for j in solved_numbers:
            section[i][j-1] = 0
    return section


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


def remove_posibilities1(posibility_matrix):
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
        unsolved_cells_before = get_unsolved_cell_indexes(posibility_matrix)
        # subtract solved numers from unsolved cells (replace with 0)

        for idx in range(9):
            remove_posibilities_from_section(get_posibility_section(
                Section.Row, idx, posibility_matrix))

        for idx in range(9):
            remove_posibilities_from_section(get_posibility_section(
                Section.Column, idx, posibility_matrix))

        for idx in range(9):
            remove_posibilities_from_section(get_posibility_section(
                Section.Box, idx, posibility_matrix))

        unsolved_cells_after = get_unsolved_cell_indexes(posibility_matrix)

        if len(unsolved_cells_before) == len(unsolved_cells_after):
            break


def remove_posibilities2(board, posibility_board):
    rows, columns, boxes = board.get_sections()

    print('Posibilities: ', np.count_nonzero(posibility_board))
    # remove posibilities from rows
    for row_index in range(9):
        unsolved_numbers, unsolved_column_indexes = board.get_unsolved_in_section(
            rows[row_index])

        for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_column_indexes):
            box = board.get_box_by_row_and_col(row_index, unsolved_index)
            column = board.get_column(unsolved_index)

            if np.isin(unsolved_number, box) or np.isin(unsolved_number, column):
                arr = posibility_board[row_index:row_index +
                                       1, unsolved_index:unsolved_index+1, :]
                arr[arr == unsolved_number] = 0

    print('Posibilities: ', np.count_nonzero(posibility_board))
    board.update_board(posibility_board)

    # remove posibilities from columns
    for column_index in range(9):
        unsolved_numbers, unsolved_row_indexes = board.get_unsolved_in_section(
            columns[column_index])

        for unsolved_number, unsolved_index in zip(unsolved_numbers, unsolved_row_indexes):
            row = board[unsolved_index:unsolved_index+1]
            box = board.get_box_by_row_and_col(column_index, unsolved_index)

            if np.isin(unsolved_number, row) or np.isin(unsolved_number, box):
                arr = posibility_board[unsolved_index:unsolved_index +
                                       1, unsolved_index:unsolved_index+1, :]
                arr[arr == unsolved_number] = 0

    # remove posibilities from boxes
    # for box_index in range(1):
    #     # print(boxes[box_index])
    #     unsolved_numbers, unsolved_indexes = get_unsolved_in_section(
    #         boxes[box_index])
