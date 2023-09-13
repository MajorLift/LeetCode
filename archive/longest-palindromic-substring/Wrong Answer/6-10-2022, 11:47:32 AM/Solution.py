// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = [0] * len(s)
        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                memo[i] = 1
            elif i > 0 and s[i - 1] == s [i + 1]:
                memo[i] = 2
        
        max_len = -float('inf')
        curr_len = 0
        for i in range(len(memo)):
            if memo[i] == 1:
                curr_len = 2
                k = 1
                while i - k >= 0 and i + 1 + k < len(s):
                    if s[i - k] == s[i + 1 + k]:
                        k += 1
                        curr_len += 2
                    else:
                        break
            elif memo[i] == 2:
                curr_len = 3
                k = 1
                while i - 1 - k >= 0 and i + 1 + k < len(s):
                    if s[i - 1 - k] == s[i + 1 + k]:
                        k += 1
                        curr_len += 2
                    else:
                        break
            if curr_len > max_len:
                max_len = curr_len
                
        return max_len