// https://leetcode.com/problems/parallel-courses

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj, indegree = [[] for _ in range(n + 1)], [+inf] + [0] * n
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        memo = dict()
        def dfs(u):
            if u in memo:
                return memo[u]
            memo[u] = -1
            longest = 1
            for v in adj[u]:
                res = dfs(v)
                if res == -1:
                    return -1
                longest = 1 + max(longest, res)
            memo[u] = longest
            return memo[u]

        return max([dfs(i) 
            for i,e in enumerate(indegree) 
            if e == 0] or [-1])