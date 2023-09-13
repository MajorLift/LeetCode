// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev, curr = [1] * n, [1] + [0] * (n - 1)
        for i in range(1, m):
            for j in range(1, n):
                curr[j] = curr[j - 1] + prev[j]
            prev = curr
        return curr[-1]