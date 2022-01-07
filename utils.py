import numpy as np

# -------------- #
# ORIGINAL BOARD #
# -------------- #


def get_sections(board):
    # array
    rows = [board[row_num] for row_num in range(len(board))]

    # matrix
    columns = [board[:, column_num:column_num + 1]
               for column_num in range(len(board))]
    # matrix
    boxes = [
        board[:3, :3], board[:3, 3:6], board[:3, 6:],
        board[3:6, :3], board[3:6, 3:6], board[3:6, 6:],
        board[6:, :3], board[6:, 3:6], board[6:, 6:]
    ]
    # c = np.squeeze(np.asarray(columns))
    # b = [box.flatten() for box in boxes]
    return (rows, columns, boxes)


def contains_duplicates(cells) -> bool:
    """
        Check if a section contains the same number more than once
        (0 is excepted)

        :param cells: array of cells
        :return:      True if section contains duplicates, otherwise False
    """
    non_zero_cells = cells[np.nonzero(cells)]
    return len(np.unique(non_zero_cells)) != len(non_zero_cells)


def is_valid_board(rows, columns, boxes) -> bool:
    """
        Check to see if every section of original board only contains unique numbers
        (except 0; which counts as a nan)

        :param rows:    array of rows
        :param columns: array of columns
        :param boxes:   array of boxes
        :return:        True if board is valid, otherwise False
    """
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


def get_unsolved_numbers_in_section(cells):
    """
        Get tuple of unsolved numbers and unsolved indexes from a section in original board (2d)
        [5 3 0 0 7 0 0 0 0] ->
        unsolved_numbers: [1 2 4 6 8 9]
        unsolved_indexes: [2 3 5 6 7 8]

        :param cells:   row, column or box from original board
        :return:        (unsolved numbers, unsolved indexes)
    """
    temp = np.arange(1, 10)
    indices = np.argwhere(np.isin(temp, cells))
    unsolved_numbers = np.delete(temp, indices)
    unsolved_indexes = np.argwhere(np.isin(cells, 0)).flatten()
    return (unsolved_numbers, unsolved_indexes)


def get_indexes_of_all_unsolved_cells(board):
    """
        Get indexes of all unsolved cells from original board.
        [[1 0 0], [0 1 0], [0 0 1]] -> [[0 1][0 2][1 0][1 2][2 0][2 1]]

        :param board:   original board
        :return:        indexes of all unsolved cells
    """
    return np.argwhere(board == 0)


def get_box_index(cell_row, cell_column):
    if cell_row < 3:  # 0, 1, 2
        if cell_column < 3:
            return 0
        if cell_column < 6:
            return 1
        return 2
    elif cell_row < 6:  # 3, 4, 5
        if cell_column < 3:
            return 3
        if cell_column < 6:
            return 4
        return 5
    else:  # 6, 7, 8
        if cell_column < 3:
            return 6
        if cell_column < 6:
            return 7
        return 8

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