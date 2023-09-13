// https://leetcode.com/problems/spiral-matrix

class Solution:
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
      m, n = len(matrix), len(matrix[0])
      i = j = cnt = num_turns = 0
      output = []
      while cnt < m * n:
         next_i, next_j = map(sum, zip((i, j), DIRECTIONS[num_turns % 4]))
         if not (0 <= next_i < m and 0 <= next_j < n) or matrix[next_i][next_j] == False:
            if cnt < m * n - 1:
               num_turns += 1
               continue
            else:
               output.append(matrix[i][j])
               break
         cnt += 1
         output.append(matrix[i][j])
         matrix[i][j] = False
         i, j = next_i, next_j
      return output