// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      matrix = deque([deque(row) for row in matrix])
      nr, nc = len(matrix), len(matrix[0])
      output = []
      while True:
         output.extend(matrix.popleft())
         nr -= 1
         if nr <= 1 or nc <= 1:
            break
         for i in range(nr):
            output.append(matrix[i].pop())
         nc -= 1
         if nr <= 1 or nc <= 1:
            break
         bottom = matrix.pop()
         bottom.reverse()
         output.extend(bottom)
         nr -= 1
         if nr <= 1 or nc <= 1:
            break
         for i in range(nr - 1, -1, -1):
            output.append(matrix[i].popleft())
         nc -= 1
         if nr <= 1 or nc <= 1:
            break
      output.extend(matrix[0] if nr == 1 else [e for row in matrix for e in row])
      return output
         
         
