// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      return matrix and [*matrix.pop(0)] + self.spiralOrder(self.rotate_ccw(matrix))

   def rotate_ccw(self, matrix: List[List[int]]):
      return matrix and self.compose(self.flip_horizontal, self.transpose)(matrix)

   def compose(self, *funcs):
      return reduce(lambda f, g: lambda x: f(g(x)), funcs)

   def flip_horizontal(self, matrix: List[List[int]]):
      return matrix[::-1]
   
   def transpose(self, matrix: List[List[int]]):
      return [[row[j] for row in matrix] for j in range(len(matrix[0]))]
   