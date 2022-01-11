import unittest
import numpy as np
from Board import Board

sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


class TestBoard(unittest.TestCase):
    def test_get_box_by_row_and_col(self):
        board = Board(sudoku_board)
        box = board.get_box_by_row_and_col(0, 0)
        np.testing.assert_array_equal(box, [5, 3, 0, 6, 0, 0, 0, 9, 8])
        box = board.get_box_by_row_and_col(1, 3)
        np.testing.assert_array_equal(box, [0, 7, 0, 1, 9, 5, 0, 0, 0])
        box = board.get_box_by_row_and_col(2, 6)
        np.testing.assert_array_equal(box, [0, 0, 0, 0, 0, 0, 0, 6, 0])
        box = board.get_box_by_row_and_col(3, 1)
        np.testing.assert_array_equal(box, [8, 0, 0, 4, 0, 0, 7, 0, 0])
        box = board.get_box_by_row_and_col(4, 5)
        np.testing.assert_array_equal(box, [0, 6, 0, 8, 0, 3, 0, 2, 0])
        box = board.get_box_by_row_and_col(5, 7)
        np.testing.assert_array_equal(box, [0, 0, 3, 0, 0, 1, 0, 0, 6])
        box = board.get_box_by_row_and_col(6, 2)
        np.testing.assert_array_equal(box, [0, 6, 0, 0, 0, 0, 0, 0, 0])
        box = board.get_box_by_row_and_col(7, 5)
        np.testing.assert_array_equal(box, [0, 0, 0, 4, 1, 9, 0, 8, 0])
        box = board.get_box_by_row_and_col(8, 8)
        np.testing.assert_array_equal(box, [2, 8, 0, 0, 0, 5, 0, 7, 9])

    def test_get_sections(self):
        board = Board(sudoku_board)
        rows, columns, boxes = board.get_sections()
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
        board = Board(sudoku_board)
        # rows, columns, boxes = board.get_sections(board)

        numbers, indexes = board.get_unsolved_in_section(board.get_row(0))
        np.testing.assert_array_equal(numbers, [1, 2, 4, 6, 8, 9])
        np.testing.assert_array_equal(indexes, [2, 3, 5, 6, 7, 8])
        numbers, indexes = board.get_unsolved_in_section(board.get_row(4))
        np.testing.assert_array_equal(numbers, [2, 5, 6, 7, 9])
        np.testing.assert_array_equal(indexes, [1, 2, 4, 6, 7])

        numbers, indexes = board.get_unsolved_in_section(board.get_column(0))
        np.testing.assert_array_equal(numbers, [1, 2, 3, 9])
        np.testing.assert_array_equal(indexes, [2, 6, 7, 8])
        numbers, indexes = board.get_unsolved_in_section(board.get_column(4))
        np.testing.assert_array_equal(numbers, [3, 4, 5])
        np.testing.assert_array_equal(indexes, [2, 4, 6])

        numbers, indexes = board.get_unsolved_in_section(board.get_box(0))
        np.testing.assert_array_equal(numbers, [1, 2, 4, 7])
        np.testing.assert_array_equal(indexes, [2, 4, 5, 6])
        numbers, indexes = board.get_unsolved_in_section(board.get_box(4))
        np.testing.assert_array_equal(numbers, [1, 4, 5, 7, 9])
        np.testing.assert_array_equal(indexes, [0, 2, 4, 6, 8])

    def test_get_indexes_of_all_unsolved_cells(self):
        board = Board(sudoku_board)
        indexes = board.get_indexes_of_all_unsolved_cells()
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

    def test_create_posibility_matrix(self):
        board = Board(sudoku_board)
        posibility_matrix = board.create_posibility_matrix(board.board)
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
