// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        @cache
        def dfs(r, c):
            max_length = 1
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c]:
                    max_length = max(max_length, 1 + dfs(i, j))
            return max_length
        
        return max(dfs(i, j) for i in range(m) for j in range(n))