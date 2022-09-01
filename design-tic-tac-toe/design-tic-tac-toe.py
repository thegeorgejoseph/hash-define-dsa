class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows, self.cols = [0] * n, [0] * n
        self.diag, self.antiDiag = 0, 0

    def move(self, row: int, col: int, player: int) -> int:
        currentPlayer = 1 if player == 1 else -1
        self.rows[row] += currentPlayer
        self.cols[col] += currentPlayer
        if row == col:
            self.diag += currentPlayer
        if col == self.n - row - 1:
            self.antiDiag += currentPlayer
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.antiDiag) == self.n:
            return player
        return 0