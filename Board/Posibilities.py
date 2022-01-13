import numpy as np
from typing import List


class Posibilities:

    def __init__(self, board: np.ndarray) -> None:
        self.matrix = self.create_posibility_matrix(board)
        self.rows = self.matrix
        self.columns = self.get_columns()
        self.boxes = self.get_boxes()

    def create_posibility_matrix(self, board: np.ndarray) -> np.ndarray:
        """
            Creates a 3d matrix from original 2d board where all cells become arrays of possible numbers.
            Each cell of the 2d board will generate a third axis in its place.
            A unsolved cell will generate an array with all possible solutions
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
        matrix = np.repeat(np.copy(board)[:, :, np.newaxis], 9, axis=2)
        all_posibilities = np.arange(1, 10)
        for i in range(9):
            for j in range(9):
                val = matrix[i:i+1, j:j+1, :1]  # 0 or a solved value
                if val == 0:
                    matrix[i:i+1, j:j+1] = all_posibilities
                else:
                    new_arr = np.zeros(9)
                    new_arr[val-1] = val
                    matrix[i:i+1, j:j+1] = new_arr
        return matrix

    def get_row(self, idx) -> np.ndarray:
        return self.rows[idx]

    def set_row(self, new_row, idx) -> None:
        self.matrix[idx:idx+1, :, :] = new_row

    def get_column(self, idx) -> np.ndarray:
        return self.matrix[:, idx:idx+1, :]

    def set_column(self, new_column, idx) -> None:
        self.matrix[:, idx:idx+1, :] = new_column

    def get_box(self, idx) -> np.ndarray:
        if idx == 0:
            return self.matrix[:3, :3, :]
        if idx == 1:
            return self.matrix[:3, 3:6, :]
        if idx == 2:
            return self.matrix[:3, 6:, :]
        if idx == 3:
            return self.matrix[3:6, :3, :]
        if idx == 4:
            return self.matrix[3:6, 3:6, :]
        if idx == 5:
            return self.matrix[3:6, 6:, :]
        if idx == 6:
            return self.matrix[6:, :3, :]
        if idx == 7:
            return self.matrix[6:, 3:6, :]
        if idx == 8:
            return self.matrix[6:, 6:, :]
        else:
            raise Exception("Box index must be between 0 and 8")

    def set_box(self, new_box, idx) -> None:
        if idx == 0:
            self.matrix[:3, :3, :] = new_box
        if idx == 1:
            self.matrix[:3, 3:6, :] = new_box
        if idx == 2:
            self.matrix[:3, 6:, :] = new_box
        if idx == 3:
            self.matrix[3:6, :3, :] = new_box
        if idx == 4:
            self.matrix[3:6, 3:6, :] = new_box
        if idx == 5:
            self.matrix[3:6, 6:, :] = new_box
        if idx == 6:
            self.matrix[6:, :3, :] = new_box
        if idx == 7:
            self.matrix[6:, 3:6, :] = new_box
        if idx == 8:
            self.matrix[6:, 6:, :] = new_box

    def get_columns(self) -> np.ndarray:
        return np.array([self.get_column(idx) for idx in range(9)])

    def get_boxes(self) -> np.ndarray:
        return np.array([self.get_box(idx) for idx in range(9)])

    def get_cell(self, indices: List[int]) -> np.ndarray:
        return self.matrix[indices[0]:indices[0]+1, indices[1]:indices[1]+1].flatten()

    def get_unsolved_cell_indices(self) -> np.ndarray:
        """
            Get an array of indices of all unsolved cells in posibility matrix
            where each index is represented by [row index, column index]
            e.g. [[0 0][0 4][3 2][3 8]]

            Returns
            -------
            ndarray: 2d array representing all unsolved cell indices
        """
        unsolved_indices = []
        for i in range(9):
            for j in range(9):
                non_zeros = np.count_nonzero(self.matrix[i:i+1, j:j+1])
                if non_zeros != 1:
                    unsolved_indices.append([i, j])
        return np.array(unsolved_indices)

    def get_solved_and_unsolved_from_section(self, section: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
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

    def remove_duplicates_from_section(self, section: np.ndarray) -> np.ndarray:
        solved_numbers, unsolved_indexes = self.get_solved_and_unsolved_from_section(
            section.reshape(9, 9))

        cp = np.copy(section).reshape(9, 9)
        for i in unsolved_indexes:
            for j in solved_numbers:
                cp[i][j-1] = 0

        return cp.reshape(section.shape)

    def remove_duplicates_from_all_sections(self) -> None:
        while True:
            unsolved_cells_before = self.get_unsolved_cell_indices()

            for idx in range(9):
                self.set_row(self.remove_duplicates_from_section(
                    self.get_row(idx)), idx)
            # for idx in range(9):
                self.set_column(self.remove_duplicates_from_section(
                    self.get_column(idx)), idx)
            # for idx in range(9):
                self.set_box(self.remove_duplicates_from_section(
                    self.get_box(idx)), idx)

            unsolved_cells_after = self.get_unsolved_cell_indices()

            if len(unsolved_cells_before) == len(unsolved_cells_after):
                break

    def __str__(self):
        return self.matrix
