// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(coord: tuple[int, int], visited: set[tuple[int, int]]) -> None:
            r, c = coord
            visited.add((r, c))
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited and heights[i][j] >= heights[r][c]:
                    dfs((i, j), visited)

        pacific, atlantic = set(), set()
        [dfs((x, y), pacific) for x, y in [*[(i, 0) for i in range(m)], *[(0, j + 1) for j in range(n - 1)]]]
        [dfs((x, y), atlantic) for x, y in [*[(i, n - 1) for i in range(m)], *[(m - 1, j) for j in range(n - 1)]]]
        return pacific & atlantic
