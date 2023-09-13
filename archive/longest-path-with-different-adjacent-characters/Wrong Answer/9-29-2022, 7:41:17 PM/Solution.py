// https://leetcode.com/problems/longest-path-with-different-adjacent-characters

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for child, node in enumerate(parent[1:]):
            children[node].append(child)
        print(children)
        
        # ans = 1
        # def dfs(n):
        #     nonlocal ans
        #     if not children[n]:
        #         return 1
            
            
            

        # dfs(0)
        # return ans