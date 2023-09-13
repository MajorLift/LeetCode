// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path

class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(maxsize=None)
        def dfs(i = 0, j = 0, counter = 0):
            if i == m or j == n or counter < 0:
                return False
            curr = grid[i][j]
            
            counter += 1 if curr == '(' else -1

            return (i, j) == (m - 1, n - 1) and counter == 1 \
                or dfs(i + 1, j, counter) or dfs(i, j + 1, counter)
                        
        return dfs()
