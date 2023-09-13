// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[None for i in range(n)] for j in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
        for i in range(n - 2):
            for j in range(i + 2, n):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        
        return len([(i, j) for i in range(n) for j in range(n) if dp[i][j]])