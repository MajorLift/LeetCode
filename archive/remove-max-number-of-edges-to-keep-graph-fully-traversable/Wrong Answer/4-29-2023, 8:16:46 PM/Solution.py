// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_a, uf_b = UnionFind(n), UnionFind(n)
        cnt_a = cnt_b = 1
        for _type, u, v in edges:
            if _type in (1, 3):
                cnt_a += uf_a.union(u, v)
            if _type in (2, 3):
                cnt_b += uf_b.union(u, v)
        if uf_a.numGroups == 1 and uf_b.numGroups == 1:
            return len(edges) - max(cnt_a, cnt_b)
        return -1

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size + 1))
        self.numEdges = 0
        self.numGroups = size
        
    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY:
            return 0
        self.roots[rootY] = rootX
        self.numEdges += 1
        self.numGroups -= 1
        return 1
    