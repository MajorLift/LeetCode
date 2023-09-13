// https://leetcode.com/problems/rotate-image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self.n = len(matrix)
        self.transpose()
        self.reflect()

    def transpose(self):
        for i in range(self.n):
            for j in range(i):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
    
    def reflect(self):
        for i, j in product(range(self.n), range(self.n // 2)):
            self.matrix[i][j], self.matrix[i][self.n - j - 1] = self.matrix[i][self.n - j - 1], self.matrix[i][j]