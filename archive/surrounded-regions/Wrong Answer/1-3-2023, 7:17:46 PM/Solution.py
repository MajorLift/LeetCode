// https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                    board[i][j] = "B"
                    dfs(i, j)

        for i, j in itertools.product((0, m - 1), (0, n - 1)):
            dfs(i, j) if board[i][j] == "O" else None

        for i, j in itertools.product(range(1, m - 1), range(1, n - 1)):
            board[i][j] = "O" if board[i][j] == "B" else "X"