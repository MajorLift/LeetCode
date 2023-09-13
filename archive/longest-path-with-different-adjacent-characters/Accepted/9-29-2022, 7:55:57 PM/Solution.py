// https://leetcode.com/problems/longest-path-with-different-adjacent-characters

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        children = [[] for _ in range(n)]
        for child, node in enumerate(parent):
            if node >= 0:
                children[node].append(child)
        # print(children)

        ans = 1
        def dfs(k):
            nonlocal ans
            if len(children[k]) == 0:
                return 1
            first, second = 0, 0
            for child in children[k]:
                curr = dfs(child)
                if s[child] != s[k]:
                    if second < curr <= first:
                        second = curr
                    elif curr > first:
                        first, second = curr, first
            ans = max(ans, first + second + 1)
            return first + 1
        dfs(0)
        return ans