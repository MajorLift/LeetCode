// https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def dfs(coord: tuple[int, int], visited: set[tuple[int, int]]) -> set[tuple[int, int]]:
            r, c = coord
            visited.add((r, c))
            for i, j in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited and heights[i][j] >= heights[r][c]:
                    dfs((i, j), visited)
            return visited

        pacific, atlantic = set(), set()
        [dfs((x, y), pacific) for x, y in [*[(i, 0) for i in range(m)], *[(0, j) for j in range(1, n)]]]
        [dfs((x, y), atlantic) for x, y in [*[(i, n - 1) for i in range(m)], *[(m - 1, j) for j in range(n - 1)]]]
        return [[i, j] for i, j in pacific.intersection(atlantic)]
