// https://leetcode.com/problems/graph-valid-tree

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        rootX = x
        while self.root[rootX] != rootX:
            rootX = self.root[rootX]
        while x != rootX:
            parent = self.root[x]
            self.root[x] = rootX
            x = parent
        return rootX
        
    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
        
    def isConnected(self, x, y):
        return self.root[x] == self.root[y]
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)
        for [x, y] in edges:
            if uf.isConnected(x, y):
                return False
            else:
                uf.union(x, y)
        return True