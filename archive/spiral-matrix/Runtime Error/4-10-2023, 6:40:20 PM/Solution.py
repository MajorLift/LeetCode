// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      matrix = deque([deque(row) for row in matrix])
      nr, nc = len(matrix), len(matrix[0])
      output = []
      while nr > 1 or nc > 1:
         print(matrix)
         output.extend(matrix.popleft())
         nr -= 1

         print(matrix)
         for i in range(nr):
            output.append(matrix[i].pop())
         nc -= 1
         
         print(matrix)
         if matrix:
            output.extend(reversed(matrix.pop()))
            nr -= 1

         print(matrix)
         for i in range(nr - 1, -1, -1):
            output.append(matrix[i].popleft())
         nc -= 1
      
      print(matrix)
      if matrix:
         output.extend(matrix[0])
      print(matrix)
      return output         
         
