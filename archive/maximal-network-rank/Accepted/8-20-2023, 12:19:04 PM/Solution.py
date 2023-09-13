// https://leetcode.com/problems/maximal-network-rank

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [[0] * n for _ in range(n)]
        for u, v in roads:
            adj[u][v] = adj[v][u] = 1
        return max(sum(adj[i]) + sum(adj[j]) - adj[i][j] 
            for i, j in product(range(n), range(n)) 
            if i < j)