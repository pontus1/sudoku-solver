import numpy as np

# -------- #
# 2D BOARD #
# -------- #


def get_sections(board: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
        Get sections from a board

        Parameters
        ----------
        board:  ndarray
            2d array of board

        Returns
        -------
        tuple:  array of 9 rows, array of 9 columns, array of 9 boxes
    """
    rows = np.array([board[row_num] for row_num in range(len(board))])

    columns = np.array([board[:, col_num:col_num + 1]
                        for col_num in range(len(board))]).reshape(9, 9)

    boxes = np.array([
        board[:3, :3], board[:3, 3:6], board[:3, 6:],
        board[3:6, :3], board[3:6, 3:6], board[3:6, 6:],
        board[6:, :3], board[6:, 3:6], board[6:, 6:]
    ]).reshape(9, 9)

    return (rows, columns, boxes)


def contains_duplicates(section: np.ndarray) -> bool:
    """
        Check if a section contains the same number more than once
        (0 does not count)

        Parameters
        ----------
        section: ndarray
            2d array - a row, column or box from board

        Returns
        -------
        bool:   True if section contains duplicates, otherwise False
    """
    non_zero_cells = section[np.nonzero(section)]
    return len(np.unique(non_zero_cells)) != len(non_zero_cells)


def is_valid_board(board: np.ndarray) -> bool:
    """
        Check to see if every section of board only contains unique numbers
        (0 does not count)

        Parameters
        ----------
        board: ndarray
            2d array of board

        Returns
        -------
        bool:   True if board is valid, otherwise False
    """
    rows, columns, boxes = get_sections(board)

    for row in rows:
        if contains_duplicates(row):
            return False
    for column in columns:
        if contains_duplicates(column):
            return False
    for box in boxes:
        if contains_duplicates(box):
            return False

    return True


def get_unsolved_in_section(section: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """
        Get a tuple of unsolved- numbers and indexes from a section in board (2d)

        Parameters
        ----------
        board: ndarray
            2d array - a row, column or box from board

        Returns
        -------
        tuple:  all unsolved numbers in section, all unsolved indexes in section

        Examples
        --------
        >>> numbers, indexes = get_unsolved_in_section([5 3 0 0 7 0 0 0 0])
        >>> numbers
        [1 2 4 6 8 9]
        >>> indexes
        [2 3 5 6 7 8]
    """
    temp = np.arange(1, 10)
    indices = np.argwhere(np.isin(temp, section))
    unsolved_numbers = np.delete(temp, indices)
    unsolved_indexes = np.argwhere(np.isin(section, 0)).flatten()
    return (unsolved_numbers, unsolved_indexes)


def get_indexes_of_all_unsolved_cells(board: np.ndarray) -> np.ndarray:
    """
        Get indexes of all unsolved cells from 2d board.

        Parameters
        ----------
        board: ndarray
            2d array of board

        Returns
        -------
        ndarray:  array containing all indexes of unsolved cells

        Examples
        --------
        Check a 3*3 board:

        >>> board = np.array([[1 0 0], [0 1 0], [0 0 1]])
        >>> indexes = get_indexes_of_all_unsolved_cells(board)
        >>> indexes
        [[0 1][0 2][1 0][1 2][2 0][2 1]]
        >>> len(indexes)
        6
    """
    return np.argwhere(board == 0)


# def get_box_index(cell_row, cell_column):
#     if cell_row < 3:  # 0, 1, 2
#         if cell_column < 3:
#             return 0
#         if cell_column < 6:
#             return 1
#         return 2
#     elif cell_row < 6:  # 3, 4, 5
#         if cell_column < 3:
#             return 3
#         if cell_column < 6:
#             return 4
#         return 5
#     else:  # 6, 7, 8
#         if cell_column < 3:
#             return 6
#         if cell_column < 6:
#             return 7
#         return 8

# ---------------- #
# POSIBILITY BOARD #
# ---------------- #


def create_posibility_board(original_board):
    # create board by copying original and adding a third dimension
    # all values will be duplicated 9 times, i.e [5] -> [5 5 5 5 5 5 5 5 5]
    pb = np.repeat(np.copy(original_board)[:, :, np.newaxis], 9, axis=2)
    # fill unsolved cells/arrays with posibilities ([0 0 0 0 0 0 0 0 0] -> [1 2 3 4 5 6 7 8 9])
    # replace solced cells/arrays with zeros exept for the solved value at that index -1 ([5 5 5 5 5 5 5 5 5] -> [0 0 0 0 5 0 0 0 0])
    posibilities = np.arange(1, 10)
    for i in range(9):
        for j in range(9):
            # current value (0 or a solved value)
            val = pb[i:i+1, j:j+1, :1]
            if val == 0:
                pb[i:i+1, j:j+1] = posibilities
            else:
                new_arr = np.zeros(9)
                new_arr[val-1] = val
                # replace with 0 at all index but right
                pb[i:i+1, j:j+1] = new_arr
    return pb


def get_unsolved_cells(posibility_board):
    # plocka ut celler/arrayer där len(non_zeros) != 1
    temp_list = []
    for i in range(9):
        for j in range(9):
            non_zeros = np.count_nonzero(posibility_board[i:i+1, j:j+1])
            if non_zeros != 1:
                temp_list.append([i, j])
    return np.array(temp_list)


def get_cell_by_index(posibility_board, cell):
    return posibility_board[cell[0]:cell[0]+1, cell[1]:cell[1]+1]


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

    return (solved_numbers, unsolved_numbers, solved_indexes, unsolved_indexes)


def subtract_imposible_numbers_from_section(cells, unsolved_indexes, solved_numbers):
    for i in unsolved_indexes:
        for j in solved_numbers:
            cells[i][j-1] = 0
    return cells


def solve_section(cells):
    solved_numbers, unsolved_numbers, solved_indexes, unsolved_indexes = get_solved_and_unsolved([
        cells])
    updated_section = subtract_imposible_numbers_from_section(
        cells, unsolved_indexes, solved_numbers)
    return updated_section


def create_solved_board(posibility_board):
    board = []
    for idx in range(9):
        row = []
        for cell in posibility_board[idx:idx+1, :, :].reshape(9, 9):
            if np.count_nonzero(cell) == 1:
                # extract solved number and add to row
                row.append(cell[np.nonzero(cell)[0].tolist()[0]])
            else:
                # append 0 (since it's npt solved)
                row.append(0)
        board.append(row)
    return np.array(board)


def get_box_by_cell_index(ridx, cidx, board):
    """
        Get a box-section by row- and column indices

        :param ridx:    row index
        :param cidx:    column index
        :param board:   board
        :return:        a box-section
    """

    if ridx < 3:
        if cidx < 3:
            return board[:3, :3]
        if cidx < 6:
            return board[:3, 3:6]
        return board[:3, 6:]
    elif ridx < 6:
        if cidx < 3:
            return board[3:6, :3]
        if cidx < 6:
            return board[3:6, 3:6]
        return board[3:6, 6:]
    else:
        if cidx < 3:
            return board[6:, :3]
        if cidx < 6:
            return board[6:, 3:6]
        return board[6:, 6:]
