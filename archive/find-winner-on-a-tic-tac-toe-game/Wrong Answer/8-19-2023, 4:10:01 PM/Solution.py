// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        self.board = [[None] * 3 for _ in range(3)]
        self.player = True
        for r, c in moves:
            self.board[r][c] = self.player
            if any([self.check_rows(r), self.check_cols(c), self.check_diags()]):
                return 'A' if self.player else 'B'
            self.player = not self.player  
        return "Draw"

    def check_rows(self, r):
        return all(self.board[r][j] == self.player for j in range(3))

    def check_cols(self, c):
        return all(self.board[i][c] == self.player for i in range(3))

    def check_diags(self):
        return all(self.board[i][i] == self.player for i in range(3)) \
            or all(self.board[i][2 - i] == self.player for i in range(3))
