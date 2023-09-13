// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

class UnionFind:
    def __init__(self, n):
        self.root = [-1 for _ in range(n)]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[y] = rootX

    def find(self, x):
        if self.root[x] == -1:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)
        return len([x for x in uf.root if x == -1])
