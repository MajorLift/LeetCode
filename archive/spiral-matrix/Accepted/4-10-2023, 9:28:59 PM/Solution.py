// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      return matrix and matrix.pop(0) + self.spiralOrder(self.rotate_ccw(matrix))

   def rotate_ccw(self, matrix: List[List[int]]):
      return matrix and self.transpose(self.reflect(matrix))

   def reflect(self, matrix: List[List[int]]):
      return [list(reversed(row)) for row in matrix]

   def transpose(self, matrix: List[List[int]]):
      return [[row[j] for row in matrix] for j in range(len(matrix[0]))]