import unittest
import numpy as np
from validation import contains_duplicates, is_valid_board
from Board.Board import Board

valid_board = Board([
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

invalid_board = Board([
    [7, 6, 2, 0, 0, 0, 0, 0, 4],
    [0, 8, 0, 0, 4, 0, 0, 0, 7],
    [0, 5, 0, 0, 2, 8, 0, 1, 0],
    [0, 0, 0, 6, 0, 4, 0, 3, 0],
    [9, 0, 6, 0, 1, 2, 0, 4, 0],
    [0, 2, 4, 0, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 7, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 8, 4, 7, 3, 0, 6, 7]
])


class TestValidation(unittest.TestCase):
    def test_contains_duplicates(self):
        self.assertTrue(contains_duplicates(
            np.array([1, 3, 0, 0, 7, 0, 0, 1, 0])))  # 1 * 2
        self.assertTrue(contains_duplicates(
            np.array([1, 3, 0, 0, 7, 5, 5, 5, 0])))  # 5 * 3
        self.assertFalse(contains_duplicates(
            np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])))  # 0 * 9
        self.assertFalse(contains_duplicates(
            np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])))  # all unique

    def test_is_valid_board(self):
        self.assertTrue(is_valid_board(valid_board))
        self.assertFalse(is_valid_board(invalid_board))


if __name__ == '__main__':
    unittest.main()
