// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      matrix = deque([deque(row) for row in matrix])
      nr, nc = len(matrix), len(matrix[0])
      output = []
      while nr > 1 or nc > 1:
         output.extend(matrix.popleft()) if matrix else None
         nr -= 1

         for i in range(nr):
            output.append(matrix[i].pop()) if matrix[i] else None
         nc -= 1
         
         output.extend(reversed(matrix.pop())) if matrix else None
         nr -= 1

         for i in range(nr - 1, -1, -1):
            output.append(matrix[i].popleft()) if matrix[i] else None
         nc -= 1
      
      output.extend(matrix[0]) if matrix else None
      return output
         
