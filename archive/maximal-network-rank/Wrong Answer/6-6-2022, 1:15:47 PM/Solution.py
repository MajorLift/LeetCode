// https://leetcode.com/problems/maximal-network-rank

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        mat = [[0 if i != j else 1 for i in range(n)] for j in range(n)]        
        for [a, b] in roads:
            mat[a][b] = 1
            mat[b][a] = 1
            
        def rank(adj_mat, a, b):
            counter = 0
            for i in range(n):
                counter += adj_mat[a][i] | adj_mat[b][i]
            return counter
            
        max = -1
        for i in range(n):
            for j in range(n):
                if i != j:
                    if rank(mat, i, j) > max:
                        max = rank(mat, i, j)
        return max
