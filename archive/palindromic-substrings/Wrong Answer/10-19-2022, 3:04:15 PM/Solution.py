// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
        for i in range(n - 2):
            for j in range(i + 2, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        return sum(len([x for x in row if x]) for row in dp)