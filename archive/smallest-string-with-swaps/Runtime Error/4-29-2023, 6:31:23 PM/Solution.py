// https://leetcode.com/problems/smallest-string-with-swaps

class Solution:
    def smallestStringWithSwaps(self, s, pairs: List[List[int]]) -> str:
        

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size))
        self.ranks = [0] * size

    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY: return