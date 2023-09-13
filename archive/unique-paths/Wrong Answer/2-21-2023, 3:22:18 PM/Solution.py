// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev, acc = [1] * n, [1] + [0] * (n - 1)
        for i in range(1, m):
            for j in range(1, n):
                acc[j] = acc[j - 1] + prev[j]
            if i < m - 1:
                prev, acc = acc, [1] + [0] * (n - 1)
        return acc[-1]