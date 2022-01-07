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

# -------------------- #
# 3D POSIBILITY MATRIX #
# -------------------- #


def get_posibility_matrix(board: np.ndarray) -> np.ndarray:
    """
        Creates a 3d matrix from original 2d board where all cells become arrays of possible numbers.
        Each cell of the 2d board will generate a third axis in its place.
        A unsolved cell will generate an array with all possibilities are included
        (0 -> [1 2 3 4 5 6 7 8 9])
        A solved cell will generate an array where all indexes are set to 0 except for index n-1
        that will be set to n
        (1 -> [1 0 0 0 0 0 0 0 0])
        (5 -> [0 0 0 0 5 0 0 0 0])

        Parameters
        ----------
        board: ndarray
            2d array of board

        Returns
        -------
        ndarray: 3d matrix representing all posibilities on board passed as arg
    """
    posibilities = np.repeat(np.copy(board)[:, :, np.newaxis], 9, axis=2)
    all_posibilities = np.arange(1, 10)
    for i in range(9):
        for j in range(9):
            val = posibilities[i:i+1, j:j+1, :1]  # 0 or a solved value
            if val == 0:
                posibilities[i:i+1, j:j+1] = all_posibilities
            else:
                new_arr = np.zeros(9)
                new_arr[val-1] = val
                posibilities[i:i+1, j:j+1] = new_arr
    return posibilities


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


def solve_section(cells):
    solved_numbers, unsolved_indexes = get_solved_and_unsolved([cells])
    updated_section = subtract_imposible_numbers_from_section(
        cells, unsolved_indexes, solved_numbers)
    return updated_section


def create_solved_board(posibility_matrix):
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
