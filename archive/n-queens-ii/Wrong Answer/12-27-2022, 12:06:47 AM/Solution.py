// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        init = [[True for _ in range(n)] for _ in range(n)]
        output = 0
        def backtrack(row, col):
            nonlocal output
            if row == n - 1:
                output += 1
                return
            
            for i in range(n):
                valids[row][i] = False  # row
                valids[i][col] = False  # col
                if col + i < n:
                    if row - i >= 0:
                        valids[row - i][col + i] = False    # anti-diag
                    if row + i < n:
                        valids[row + i][col + i] = False    # diag

            for i in range(n):
                if valids[row + 1][i]:
                    backtrack(row + 1, i)

        for i in range(n):
            valids = copy.deepcopy(init)
            backtrack(0, i)
        return output