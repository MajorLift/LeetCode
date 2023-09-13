// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        def dfs(start = (0, 0), counter = 1):
            i, j = start[0], start[1]
            if i == m or j == n or counter < 0:
                return False
            curr = grid[i][j]
            
            if curr == '(':
                counter += 1
            else:
                counter -= 1

            if (i, j) == (m - 1, n - 1) and counter == 1:
                return True            
            
            return dfs((i + 1, j), counter) or dfs((i, j + 1), counter)
                        
        return dfs()
