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
        print(bin(r), bin(c))

        for i, j in product(range(m), range(n)):
            if r & 1 << i | c & 1 << j:
                matrix[i][j] = 0
