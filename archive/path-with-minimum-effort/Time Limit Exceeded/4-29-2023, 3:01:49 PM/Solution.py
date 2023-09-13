// https://leetcode.com/problems/path-with-minimum-effort

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = map(len, (heights, heights[0]))
        DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        edges = []
        for r, c in product(range(m), range(n)):
            for i, j in (map(sum, zip((r, c), d)) for d in DIRECTIONS):
                if not (0 <= i < m and 0 <= j < n):
                    continue
                heappush(edges, (abs(heights[r][c] - heights[i][j]), (r, c), (i, j)))
        
        uf = UnionFind(m, n)
        effort = 0
        while edges:
            while edges and edges[0][0] == effort:
                _, x, y = heappop(edges)
                uf.union(x, y)
            if uf.isConnected((0, 0), (m - 1, n - 1)):
                break
            effort += 1
        return effort
        

class UnionFind:
    def __init__(self, m, n):
        self.roots = [[(i, j) for j in range(n)] for i in range(m)]
        
    def find(self, x):
        i, j = x
        if self.roots[i][j] == (i, j):
            return (i, j)
        self.roots[i][j] = self.find(self.roots[i][j])
        return self.roots[i][j]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        i, j = rootY
        self.roots[i][j] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)