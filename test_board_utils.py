import unittest
import numpy as np
import board_utils as utils

board = np.array([
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
])


class BoardUtils(unittest.TestCase):
    def test_get_sections(self):
        rows, columns, boxes = utils.get_sections(board)
        np.testing.assert_array_equal(rows[0], [5, 3, 0, 0, 7, 0, 0, 0, 0])
        np.testing.assert_array_equal(rows[1], [6, 0, 0, 1, 9, 5, 0, 0, 0])
        np.testing.assert_array_equal(rows[2], [0, 9, 8, 0, 0, 0, 0, 6, 0])
        np.testing.assert_array_equal(rows[3], [8, 0, 0, 0, 6, 0, 0, 0, 3])
        np.testing.assert_array_equal(rows[4], [4, 0, 0, 8, 0, 3, 0, 0, 1])
        np.testing.assert_array_equal(rows[5], [7, 0, 0, 0, 2, 0, 0, 0, 6])
        np.testing.assert_array_equal(rows[6], [0, 6, 0, 0, 0, 0, 2, 8, 0])
        np.testing.assert_array_equal(rows[7], [0, 0, 0, 4, 1, 9, 0, 0, 5])
        np.testing.assert_array_equal(rows[8], [0, 0, 0, 0, 8, 0, 0, 7, 9])

        np.testing.assert_array_equal(columns[0], [5, 6, 0, 8, 4, 7, 0, 0, 0])
        np.testing.assert_array_equal(columns[1], [3, 0, 9, 0, 0, 0, 6, 0, 0])
        np.testing.assert_array_equal(columns[2], [0, 0, 8, 0, 0, 0, 0, 0, 0])
        np.testing.assert_array_equal(columns[3], [0, 1, 0, 0, 8, 0, 0, 4, 0])
        np.testing.assert_array_equal(columns[4], [7, 9, 0, 6, 0, 2, 0, 1, 8])
        np.testing.assert_array_equal(columns[5], [0, 5, 0, 0, 3, 0, 0, 9, 0])
        np.testing.assert_array_equal(columns[6], [0, 0, 0, 0, 0, 0, 2, 0, 0])
        np.testing.assert_array_equal(columns[7], [0, 0, 6, 0, 0, 0, 8, 0, 7])
        np.testing.assert_array_equal(columns[8], [0, 0, 0, 3, 1, 6, 0, 5, 9])

        np.testing.assert_array_equal(boxes[0], [5, 3, 0, 6, 0, 0, 0, 9, 8])
        np.testing.assert_array_equal(boxes[1], [0, 7, 0, 1, 9, 5, 0, 0, 0])
        np.testing.assert_array_equal(boxes[2], [0, 0, 0, 0, 0, 0, 0, 6, 0])
        np.testing.assert_array_equal(boxes[3], [8, 0, 0, 4, 0, 0, 7, 0, 0])
        np.testing.assert_array_equal(boxes[4], [0, 6, 0, 8, 0, 3, 0, 2, 0])
        np.testing.assert_array_equal(boxes[5], [0, 0, 3, 0, 0, 1, 0, 0, 6])
        np.testing.assert_array_equal(boxes[6], [0, 6, 0, 0, 0, 0, 0, 0, 0])
        np.testing.assert_array_equal(boxes[7], [0, 0, 0, 4, 1, 9, 0, 8, 0])
        np.testing.assert_array_equal(boxes[8], [2, 8, 0, 0, 0, 5, 0, 7, 9])

    def test_get_unsolved_in_section(self):
        rows, columns, boxes = utils.get_sections(board)

        numbers, indexes = utils.get_unsolved_in_section(rows[0])
        np.testing.assert_array_equal(numbers, [1, 2, 4, 6, 8, 9])
        np.testing.assert_array_equal(indexes, [2, 3, 5, 6, 7, 8])
        numbers, indexes = utils.get_unsolved_in_section(rows[4])
        np.testing.assert_array_equal(numbers, [2, 5, 6, 7, 9])
        np.testing.assert_array_equal(indexes, [1, 2, 4, 6, 7])

        numbers, indexes = utils.get_unsolved_in_section(columns[0])
        np.testing.assert_array_equal(numbers, [1, 2, 3, 9])
        np.testing.assert_array_equal(indexes, [2, 6, 7, 8])
        numbers, indexes = utils.get_unsolved_in_section(columns[4])
        np.testing.assert_array_equal(numbers, [3, 4, 5])
        np.testing.assert_array_equal(indexes, [2, 4, 6])

        numbers, indexes = utils.get_unsolved_in_section(boxes[0])
        np.testing.assert_array_equal(numbers, [1, 2, 4, 7])
        np.testing.assert_array_equal(indexes, [2, 4, 5, 6])
        numbers, indexes = utils.get_unsolved_in_section(boxes[4])
        np.testing.assert_array_equal(numbers, [1, 4, 5, 7, 9])
        np.testing.assert_array_equal(indexes, [0, 2, 4, 6, 8])

    def test_get_indexes_of_all_unsolved_cells(self):
        indexes = utils.get_indexes_of_all_unsolved_cells(board)
        np.testing.assert_array_equal(
            indexes, [
                [0, 2], [0, 3], [0, 5], [0, 6], [0, 7], [0, 8],
                [1, 1], [1, 2], [1, 6], [1, 7], [1, 8],
                [2, 0], [2, 3], [2, 4], [2, 5], [2, 6], [2, 8],
                [3, 1], [3, 2], [3, 3], [3, 5], [3, 6], [3, 7],
                [4, 1], [4, 2], [4, 4], [4, 6], [4, 7],
                [5, 1], [5, 2], [5, 3], [5, 5], [5, 6], [5, 7],
                [6, 0], [6, 2], [6, 3], [6, 4], [6, 5], [6, 8],
                [7, 0], [7, 1], [7, 2], [7, 6], [7, 7],
                [8, 0], [8, 1], [8, 2], [8, 3], [8, 5], [8, 6]
            ])

    def test_get_column_by_index(self):
        column = utils.get_column_by_index(0, board)
        np.testing.assert_array_equal(column, [5, 6, 0, 8, 4, 7, 0, 0, 0])
        column = utils.get_column_by_index(1, board)
        np.testing.assert_array_equal(column, [3, 0, 9, 0, 0, 0, 6, 0, 0])
        column = utils.get_column_by_index(2, board)
        np.testing.assert_array_equal(column, [0, 0, 8, 0, 0, 0, 0, 0, 0])
        column = utils.get_column_by_index(3, board)
        np.testing.assert_array_equal(column, [0, 1, 0, 0, 8, 0, 0, 4, 0])
        column = utils.get_column_by_index(4, board)
        np.testing.assert_array_equal(column, [7, 9, 0, 6, 0, 2, 0, 1, 8])
        column = utils.get_column_by_index(5, board)
        np.testing.assert_array_equal(column, [0, 5, 0, 0, 3, 0, 0, 9, 0])
        column = utils.get_column_by_index(6, board)
        np.testing.assert_array_equal(column, [0, 0, 0, 0, 0, 0, 2, 0, 0])
        column = utils.get_column_by_index(7, board)
        np.testing.assert_array_equal(column, [0, 0, 6, 0, 0, 0, 8, 0, 7])
        column = utils.get_column_by_index(8, board)
        np.testing.assert_array_equal(column, [0, 0, 0, 3, 1, 6, 0, 5, 9])

    def test_get_box_by_cell_indexes(self):
        box = utils.get_box_by_cell_indexes(0, 0, board)
        np.testing.assert_array_equal(box, [5, 3, 0, 6, 0, 0, 0, 9, 8])
        box = utils.get_box_by_cell_indexes(1, 3, board)
        np.testing.assert_array_equal(box, [0, 7, 0, 1, 9, 5, 0, 0, 0])
        box = utils.get_box_by_cell_indexes(2, 6, board)
        np.testing.assert_array_equal(box, [0, 0, 0, 0, 0, 0, 0, 6, 0])
        box = utils.get_box_by_cell_indexes(3, 1, board)
        np.testing.assert_array_equal(box, [8, 0, 0, 4, 0, 0, 7, 0, 0])
        box = utils.get_box_by_cell_indexes(4, 5, board)
        np.testing.assert_array_equal(box, [0, 6, 0, 8, 0, 3, 0, 2, 0])
        box = utils.get_box_by_cell_indexes(5, 7, board)
        np.testing.assert_array_equal(box, [0, 0, 3, 0, 0, 1, 0, 0, 6])
        box = utils.get_box_by_cell_indexes(6, 2, board)
        np.testing.assert_array_equal(box, [0, 6, 0, 0, 0, 0, 0, 0, 0])
        box = utils.get_box_by_cell_indexes(7, 5, board)
        np.testing.assert_array_equal(box, [0, 0, 0, 4, 1, 9, 0, 8, 0])
        box = utils.get_box_by_cell_indexes(8, 8, board)
        np.testing.assert_array_equal(box, [2, 8, 0, 0, 0, 5, 0, 7, 9])

    def test_create_posibility_matrix(self):
        posibility_matrix = utils.create_posibility_matrix(board)
        print(posibility_matrix)
        np.testing.assert_array_equal(posibility_matrix, [
            [
                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ],
            [
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 3, 0, 0, 0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 3, 0, 0, 0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 0, 0, 0, 0, 0, 0, 0, 0]
            ],
            [
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0]
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9]
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 5, 0, 0, 0, 0]
            ],
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9]
            ],
        ])


if __name__ == '__main__':
    unittest.main()
