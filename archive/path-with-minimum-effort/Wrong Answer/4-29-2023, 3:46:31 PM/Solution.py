// https://leetcode.com/problems/path-with-minimum-effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        def dfs(r, c, effort, visited):
            if (r, c) == (m - 1, n - 1):
                return True
            visited |= 1 << r * m + c
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n) \
                    or visited & 1 << i * m + j \
                    or abs(heights[i][j] - heights[r][c]) > effort:
                    continue
                if dfs(i, j, effort, visited):
                    return True
            return False

        return bisect_left(list(range(10 ** 6)), True, 
            key=lambda x: dfs(0, 0, x, 2 ** (m * n)))
