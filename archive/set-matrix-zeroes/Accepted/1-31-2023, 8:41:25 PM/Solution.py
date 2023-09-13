// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        zeros = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.add((i, j))

        for r, c in zeros:
            for k in range(m):
                matrix[k][c] = 0
            for h in range(n):
                matrix[r][h] = 0