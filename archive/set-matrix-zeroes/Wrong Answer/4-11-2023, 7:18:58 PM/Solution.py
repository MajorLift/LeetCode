// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        r = c = 0
        for i, j in product(range(m), range(n)):
            if matrix[i][j] == 0:
                r |= 1 << i
                c |= 1 << j
                
        for i in range(m):
            if r & 1 << i:
                for j in range(m):
                    matrix[i][j] = 0

        for j in range(n):
            if c & 1 << j:
                for i in range(m):
                    matrix[i][j] = 0
        