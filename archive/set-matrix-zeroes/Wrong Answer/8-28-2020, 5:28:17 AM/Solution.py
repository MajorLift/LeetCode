// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        for i,p in enumerate(matrix):
            if i == 0:
                pass
            for j,q in enumerate(matrix[i]):
                if j == 0:
                    pass
                if q == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        firstrow = matrix[0]
        firstcol = [matrix[i][0] for i in range(m)]

        for i,p in enumerate(firstcol):
            if i == 0:
                pass
            if p == 0:
                matrix[i] = [0]*n
        for j,q in enumerate(firstrow):
            if j == 0:
                pass
            if q == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
            