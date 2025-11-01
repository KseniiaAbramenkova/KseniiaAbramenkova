import unittest

# Game initialization (logic without graphics)
BOARD_ROWS, BOARD_COLS = 3, 3

def check_winner(board):
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if None in row:
            return False
    return True

def check_win_or_block(board, player):
    for row in range(BOARD_ROWS):
        # Check rows
        if board[row].count(player) == 2 and board[row].count(None) == 1:
            return row, board[row].index(None)
    for col in range(BOARD_COLS):
        # Check columns
        column = [board[row][col] for row in range(BOARD_ROWS)]
        if column.count(player) == 2 and column.count(None) == 1:
            return column.index(None), col
    # Check main diagonal
    diag1 = [board[i][i] for i in range(BOARD_ROWS)]
    if diag1.count(player) == 2 and diag1.count(None) == 1:
        return diag1.index(None), diag1.index(None)
    # Check secondary diagonal
    diag2 = [board[i][BOARD_COLS - i - 1] for i in range(BOARD_ROWS)]
    if diag2.count(player) == 2 and diag2.count(None) == 1:
        return diag2.index(None), BOARD_COLS - diag2.index(None) - 1
    return None

def restart_game():
    return [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]


class TestTicTacToe(unittest.TestCase):

    # Tests to check the winner
    def test_check_winner_horizontal(self):
        board = [
            [1, 1, 1],
            [None, 2, None],
            [None, 2, None]
        ]
        self.assertEqual(check_winner(board), 1)

    def test_check_winner_vertical(self):
        board = [
            [1, None, None],
            [1, 2, None],
            [1, 2, None]
        ]
        self.assertEqual(check_winner(board), 1)

    def test_check_winner_diagonal(self):
        board = [
            [1, None, 2],
            [None, 1, 2],
            [None, None, 1]
        ]
        self.assertEqual(check_winner(board), 1)

    # Tests to check if the board is full
    def test_is_full_true(self):
        board = [
            [1, 2, 1],
            [2, 1, 2],
            [1, 2, 1]
        ]
        self.assertTrue(is_full(board))

    def test_is_full_false(self):
        board = [
            [1, 2, 1],
            [2, None, 2],
            [1, 2, 1]
        ]
        self.assertFalse(is_full(board))

    # Tests to check if a win or block move is possible
    def test_check_win_or_block_win(self):
        board = [
            [1, 1, None],
            [2, 2, 1],
            [None, 2, None]
        ]
        self.assertEqual(check_win_or_block(board, 1), (0, 2))  # Player 1 can win by placing at (0, 2)

    def test_check_win_or_block_no_move(self):
        board = [
            [1, 1, 2],
            [2, 2, 1],
            [1, 1, 2]
        ]
        self.assertIsNone(check_win_or_block(board, 1))  # No winning or blocking move for player 1

    def test_check_win_or_block_tie(self):
        board = [
            [1, 2, 1],
            [2, 1, 2],
            [1, 2, 1]
        ]
        self.assertIsNone(check_win_or_block(board, 1))  # No winning or blocking move for player 1 (tie)

    # Tests to restart the game
    def test_restart_game(self):
        board = [
            [1, 1, 1],
            [2, 2, 2],
            [None, None, None]
        ]
        new_board = restart_game()
        self.assertEqual(new_board, [[None, None, None], [None, None, None], [None, None, None]])

    def test_restart_game_empty(self):
        new_board = restart_game()
        self.assertEqual(new_board, [[None, None, None], [None, None, None], [None, None, None]])

    def test_restart_game_after_move(self):
        board = [
            [1, 2, 1],
            [2, 1, 2],
            [None, 2, None]
        ]
        new_board = restart_game()
        self.assertEqual(new_board, [[None, None, None], [None, None, None], [None, None, None]])

if __name__ == '__main__':
    unittest.main()
