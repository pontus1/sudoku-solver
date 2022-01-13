import numpy as np


class Board:

    def __init__(self, board: list[list]) -> None:
        self.board = np.array(board)
        self.rows = self.get_rows()
        self.columns = self.get_columns()
        self.boxes = self.get_boxes()

    def get_rows(self) -> np.ndarray:
        return np.array([self.board[row_num]
                         for row_num in range(len(self.board))])

    def get_columns(self) -> np.ndarray:
        return np.array([self.board[:, col_num:col_num + 1]
                         for col_num in range(len(self.board))]).reshape(9, 9)

    def get_boxes(self) -> np.ndarray:
        return np.array([
            self.board[:3, :3], self.board[:3, 3:6], self.board[:3, 6:],
            self.board[3:6, :3], self.board[3:6, 3:6], self.board[3:6, 6:],
            self.board[6:, :3], self.board[6:, 3:6], self.board[6:, 6:]
        ]).reshape(9, 9)

    def get_row(self, idx):
        return self.rows[idx]

    def get_column(self, idx):
        return self.columns[idx]

    def get_box(self, idx):
        return self.boxes[idx]

    def get_box_by_row_and_col(self, ridx, cidx):
        if ridx < 3:
            if cidx < 3:
                return self.board[:3, :3].reshape(9)
            if cidx < 6:
                return self.board[:3, 3:6].reshape(9)
            return self.board[:3, 6:].reshape(9)
        elif ridx < 6:
            if cidx < 3:
                return self.board[3:6, :3].reshape(9)
            if cidx < 6:
                return self.board[3:6, 3:6].reshape(9)
            return self.board[3:6, 6:].reshape(9)
        else:
            if cidx < 3:
                return self.board[6:, :3].reshape(9)
            if cidx < 6:
                return self.board[6:, 3:6].reshape(9)
            return self.board[6:, 6:].reshape(9)

    def get_sections(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
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

        return (self.rows, self.columns, self.boxes)

    def get_unsolved_in_section(self, section: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
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

    def get_indexes_of_all_unsolved_cells(self):
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
        return np.argwhere(self.board == 0)

    def update_board(self, posibility_matrix: np.ndarray):
        board = []
        for idx in range(9):
            row = []
            for cell in posibility_matrix[idx:idx+1, :, :].reshape(9, 9):
                if np.count_nonzero(cell) == 1:
                    # extract solved number and add to row
                    row.append(cell[np.nonzero(cell)[0].tolist()[0]])
                else:
                    # append 0 (since it's not solved)
                    row.append(0)
            board.append(row)

        self.board = np.array(board)
        self.rows = self.get_rows()
        self.columns = self.get_columns()
        self.boxes = self.get_boxes()

    def __str__(self):
        return (f'{self.board}\n')

    def __len__(self):
        return len(self.get_indexes_of_all_unsolved_cells())
