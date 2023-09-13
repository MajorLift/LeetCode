// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries.sort(key=lambda x: x[2])
        uf = UnionFind(n)
        answer = []
        for p, q, limit in queries:
            if not edgeList:
                break
            while edgeList and edgeList[0][2] < limit:
                u, v, _ = edgeList.pop()
                uf.union(u, v)
            answer.append(uf.isConnected(p, q))
        return answer + [False] * (len(queries) - len(answer))

class UnionFind:
    def __init__(self, size):
        self.roots = list(range(size))

    def find(self, x):
        if self.roots[x] == x:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        rootX, rootY = map(self.find, (x, y))
        if rootX == rootY:
            return
        self.roots[rootY] = rootX

    def isConnected(self, x, y):
        return self.find(x) == self.find(y)