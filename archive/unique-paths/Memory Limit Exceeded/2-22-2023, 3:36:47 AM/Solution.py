// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return len(list(combinations([0] * (m + n - 2), m - 1)))