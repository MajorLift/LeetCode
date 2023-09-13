// https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mst = UnionFind()
        for _, i, j in sorted([(grid[i][j], i, j) for i in range(n) for j in range(n)]):
            if mst.connected((0, 0), (n - 1, n - 1)):
                break
            min_w = +math.inf
            min_neighbor = (0, 0)
            for x, y in ((i - 1, j), (i + 1 , j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and not mst.connected((i, j), (x, y)) and grid[x][y] < min_w:
                    min_w = grid[x][y]
                    min_neighbor = (x, y)
            mst.union((i, j), min_neighbor)
        return max(grid[r][c] for (r, c) in mst.roots.keys())

class UnionFind:
    def __init__(self):
        self.roots = dict()
    
    def find(self, x):
        if x not in self.roots:
            return None
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        if x not in self.roots:
            self.roots[x] = x
        if y not in self.roots:
            self.roots[y] = y
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.roots[rootX] = rootY
    
    def connected(self, x, y):
        return x in self.roots and y in self.roots and self.find(x) == self.find(y)
