// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[False if i != j else True for i in range(length)] for j in range(length)]
        
        for k in range(length - 1):
            if s[k] == s[k + 1]:
                dp[k][k + 1] = True
        for i in range(length - 1):
            for j in range(1, length):
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        
        maxlen = 0
        maxsubstr = ''
        for i in range(length):
            for j in range(length):
                currlen = j - i + 1
                if dp[i][j] and currlen > maxlen:
                    maxlen = currlen
                    maxsubstr = s[i:j + 1]
        return maxsubstr