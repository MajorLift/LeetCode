// https://leetcode.com/problems/maximal-network-rank

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        self.adj_mat = [[0 if i != j else 1 for i in range(n)] for j in range(n)]        
        for [a, b] in roads:
            self.adj_mat[a][b] = 1
            self.adj_mat[b][a] = 1
            
        def rank(a, b):
            counter = 0
            for i in range(n):
                counter += self.adj_mat[a][i] + self.adj_mat[b][i]
            counter -= self.adj_mat[a][b] + 2
            return counter
            
        max = -1
        for i in range(n):
            for j in range(i + 1, n):
                curr_rank = rank(i, j)
                if curr_rank > max:
                    max = curr_rank
        return max
