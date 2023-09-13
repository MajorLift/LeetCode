// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        init = [[True for _ in range(n)] for _ in range(n)]
        output = 0
        def backtrack(row, col, valids):
            nonlocal output
            if row == n - 1:
                output += 1
                return
            
            for i in range(n):
                valids[row][i] = False  # row
                valids[i][col] = False  # col
                if row + i < n:
                    if col + i < n:
                        valids[row + i][col + i] = False    # diag
                    if col - i >= 0:
                        valids[row + i][col - i] = False    # anti-diag

            for i in range(n):
                if valids[row + 1][i]:
                    backtrack(row + 1, i, copy.deepcopy(valids))

        for i in range(n):
            backtrack(0, i, copy.deepcopy(init))
        return output