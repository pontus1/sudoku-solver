import unittest
import numpy as np
from Board import Board
from Posibilities import Posibilities

board = Board([
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


class TestPosibilities(unittest.TestCase):
    def test_init(self):
        posibilities = Posibilities(board.board)
        np.testing.assert_array_equal(posibilities.matrix, [
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
        # COLUMNS
        np.testing.assert_array_equal(posibilities.columns[0], [
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.columns[1], [
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.columns[2], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.columns[3], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.columns[4], [
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
        ])
        np.testing.assert_array_equal(posibilities.columns[5], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.columns[6], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.columns[7], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
        ])
        np.testing.assert_array_equal(posibilities.columns[8], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
        ])
        # BOXES
        np.testing.assert_array_equal(posibilities.boxes[0], [
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
        ])
        np.testing.assert_array_equal(posibilities.boxes[1], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.boxes[2], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.boxes[3], [
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.boxes[4], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.boxes[5], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
        ])
        np.testing.assert_array_equal(posibilities.boxes[6], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.boxes[7], [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
        ])
        np.testing.assert_array_equal(posibilities.boxes[8], [
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
        ])

    def test_get_cell(self):
        posibilities = Posibilities(board.board)
        cell = posibilities.get_cell([4, 5])
        np.testing.assert_array_equal(cell, [0, 0, 3, 0, 0, 0, 0, 0, 0])

    def test_get_unsolved_cell_indices(self):
        posibilities = Posibilities(board.board)
        unsolved_cells = posibilities.get_unsolved_cell_indices()
        np.testing.assert_array_equal(unsolved_cells, [
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

    def test_get_solved_and_unsolved_from_section(self):
        posibilities = Posibilities(board.board)

        solved_numbers, unsolved_indexes = posibilities.get_solved_and_unsolved_from_section(
            posibilities.get_row(0))
        np.testing.assert_array_equal(solved_numbers, [5, 3, 7])
        np.testing.assert_array_equal(unsolved_indexes, [2, 3, 5, 6, 7, 8])

        solved_numbers, unsolved_indexes = posibilities.get_solved_and_unsolved_from_section(
            posibilities.get_row(4))
        np.testing.assert_array_equal(solved_numbers, [4, 8, 3, 1])
        np.testing.assert_array_equal(unsolved_indexes, [1, 2, 4, 6, 7])

        solved_numbers, unsolved_indexes = posibilities.get_solved_and_unsolved_from_section(
            posibilities.get_column(0))
        np.testing.assert_array_equal(solved_numbers, [5, 6, 8, 4, 7])
        np.testing.assert_array_equal(unsolved_indexes, [2, 6, 7, 8])

        solved_numbers, unsolved_indexes = posibilities.get_solved_and_unsolved_from_section(
            posibilities.get_column(6))
        np.testing.assert_array_equal(solved_numbers, [2])
        np.testing.assert_array_equal(
            unsolved_indexes, [0, 1, 2, 3, 4, 5, 7, 8])

        # solved_numbers, unsolved_indexes = posibilities.get_solved_and_unsolved_from_section(
        #     posibilities.get_box(0))
        # np.testing.assert_array_equal(solved_numbers, [5, 3, 6, 9, 8])
        # np.testing.assert_array_equal(unsolved_indexes, [2, 4, 5, 6])

        # solved_numbers, unsolved_indexes = posibilities.get_solved_and_unsolved_from_section(
        #     posibilities.get_box(8))
        # np.testing.assert_array_equal(solved_numbers, [2, 8, 5, 7, 9])
        # np.testing.assert_array_equal(unsolved_indexes, [2, 3, 4, 6])

    def test_remove_duplicates_from_section(self):
        posibilities = Posibilities(board.board)
        section = posibilities.get_row(0)
        posibilities.remove_duplicates_from_section(section)
        np.testing.assert_array_equal(section, [
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 3, 0, 0, 0, 0, 0, 0],
            [1, 2, 0, 4, 0, 6, 0, 8, 9],
            [1, 2, 0, 4, 0, 6, 0, 8, 9],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [1, 2, 0, 4, 0, 6, 0, 8, 9],
            [1, 2, 0, 4, 0, 6, 0, 8, 9],
            [1, 2, 0, 4, 0, 6, 0, 8, 9],
            [1, 2, 0, 4, 0, 6, 0, 8, 9]
        ])
        posibilities = Posibilities(board.board)
        posibilities.remove_duplicates_from_section(posibilities.get_column(0))
        np.testing.assert_array_equal(posibilities.get_column(0), [
            [0, 0, 0, 0, 5, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 6, 0, 0, 0],
            [1, 2, 3, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [0, 0, 0, 4, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 7, 0, 0],
            [1, 2, 3, 0, 0, 0, 0, 0, 9],
            [1, 2, 3, 0, 0, 0, 0, 0, 9],
            [1, 2, 3, 0, 0, 0, 0, 0, 9],
        ])
        # posibilities = Posibilities(board.board)
        # posibilities.remove_duplicates_from_section(
        #     posibilities.matrix[:3, :3, :].reshape(9, 9))
        # print(posibilities.matrix[:3, :3, :].reshape(9, 9))
        # np.testing.assert_array_equal(posibilities.matrix[:3, :3, :].reshape(9, 9), [
        #     [0, 0, 0, 0, 5, 0, 0, 0, 0],
        #     [0, 0, 3, 0, 0, 0, 0, 0, 0],
        #     [1, 2, 0, 4, 0, 0, 7, 0, 0],
        #     [0, 0, 0, 0, 0, 6, 0, 0, 0],
        #     [1, 2, 0, 4, 0, 0, 7, 0, 0],
        #     [1, 2, 0, 4, 0, 0, 7, 0, 0],
        #     [1, 2, 0, 4, 0, 0, 7, 0, 0],
        #     [0, 0, 0, 0, 0, 0, 0, 0, 9],
        #     [0, 0, 0, 0, 0, 0, 0, 8, 0],
        # ])

    def test_remove_duplicates_from_all_sections(self):
        posibilities = Posibilities(board.board)
        posibilities.remove_duplicates_from_all_sections()
        print(posibilities.matrix)
        np.testing.assert_array_equal(posibilities.matrix, [
            [
                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                [0, 0, 3, 0, 0, 0, 0, 0, 0],
                [1, 2, 0, 4, 0, 6, 0, 8, 9],
                [1, 2, 0, 4, 0, 6, 0, 8, 9],
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [1, 2, 0, 4, 0, 6, 0, 8, 9],
                [1, 2, 0, 4, 0, 6, 0, 8, 9],
                [1, 2, 0, 4, 0, 6, 0, 8, 9],
                [1, 2, 0, 4, 0, 6, 0, 8, 9],
            ],
            [
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [0, 2, 3, 4, 0, 0, 7, 8, 0],
                [0, 2, 3, 4, 0, 0, 7, 8, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 5, 0, 0, 0, 0],
                [0, 2, 3, 4, 0, 0, 7, 8, 0],
                [0, 2, 3, 4, 0, 0, 7, 8, 0],
                [0, 2, 3, 4, 0, 0, 7, 8, 0],
            ],
            [
                [1, 2, 3, 4, 5, 0, 7, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 0, 7, 0, 0],
                [1, 2, 3, 4, 5, 0, 7, 0, 0],
                [1, 2, 3, 4, 5, 0, 7, 0, 0],
                [1, 2, 3, 4, 5, 0, 7, 0, 0],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 0, 7, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 0, 4, 5, 0, 7, 0, 9],
                [1, 2, 0, 4, 5, 0, 7, 0, 9],
                [1, 2, 0, 4, 5, 0, 7, 0, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 2, 0, 4, 5, 0, 7, 0, 9],
                [1, 2, 0, 4, 5, 0, 7, 0, 9],
                [1, 2, 0, 4, 5, 0, 7, 0, 9],
                [0, 0, 3, 0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 5, 6, 7, 0, 9],
                [0, 2, 0, 0, 5, 6, 7, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [0, 2, 0, 0, 5, 6, 7, 0, 9],
                [0, 0, 3, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 5, 6, 7, 0, 9],
                [0, 2, 0, 0, 5, 6, 7, 0, 9],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [1, 0, 3, 4, 5, 0, 0, 8, 9],
                [1, 0, 3, 4, 5, 0, 0, 8, 9],
                [1, 0, 3, 4, 5, 0, 0, 8, 9],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 3, 4, 5, 0, 0, 8, 9],
                [1, 0, 3, 4, 5, 0, 0, 8, 9],
                [1, 0, 3, 4, 5, 0, 0, 8, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
            ],
            [
                [1, 0, 3, 4, 5, 0, 7, 0, 9],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [1, 0, 3, 4, 5, 0, 7, 0, 9],
                [1, 0, 3, 4, 5, 0, 7, 0, 9],
                [1, 0, 3, 4, 5, 0, 7, 0, 9],
                [1, 0, 3, 4, 5, 0, 7, 0, 9],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 0, 3, 4, 5, 0, 7, 0, 9],
            ],
            [
                [0, 2, 3, 0, 0, 6, 7, 8, 0],
                [0, 2, 3, 0, 0, 6, 7, 8, 0],
                [0, 2, 3, 0, 0, 6, 7, 8, 0],
                [0, 0, 0, 4, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
                [0, 2, 3, 0, 0, 6, 7, 8, 0],
                [0, 2, 3, 0, 0, 6, 7, 8, 0],
                [0, 0, 0, 0, 5, 0, 0, 0, 0],
            ],
            [
                [1, 2, 3, 4, 5, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 8, 0],
                [1, 2, 3, 4, 5, 6, 0, 0, 0],
                [1, 2, 3, 4, 5, 6, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 7, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 9],
            ]
        ])


if __name__ == '__main__':
    unittest.main()