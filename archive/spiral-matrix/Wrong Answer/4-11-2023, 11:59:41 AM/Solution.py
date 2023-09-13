// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      m, n = len(matrix), len(matrix[0])
      left, right, top, bottom = 0, n - 1, 0, m - 1
      output = []
      while len(output) < m * n:
         for j in range(left, right + 1):
            output.append(matrix[top][j])
         top += 1

         for i in range(top, bottom + 1):
            output.append(matrix[i][right])
         right -= 1
         
         if top >= bottom:
            break
         for j in range(right, left - 1, -1):
            output.append(matrix[bottom][j])
         bottom -= 1
         
         if left >= right:
            break
         for i in range(bottom, top - 1, -1):
            output.append(matrix[i][left])
         left += 1
         
      return output