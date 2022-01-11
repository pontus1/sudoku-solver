from Board import Board
import numpy as np


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


def is_valid_board(board) -> bool:
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
    rows, columns, boxes = board.get_sections()

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
