// https://leetcode.com/problems/n-queens-ii

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diags, antidiags = set(), set(), set()

        output = 0
        def backtrack(row):
            nonlocal output
            if row == n:
                output += 1
                return
            
            for col in range(n):
                if col in cols or row - col in diags or row + col in antidiags:
                    continue

                cols.add(col)
                diags.add(row - col)
                antidiags.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diags.remove(row - col)
                antidiags.remove(row + col)

        backtrack(0)
        return output