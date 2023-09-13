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
        output = ""
        for i in range(len(memo)):
            curr_len = 0
            left, right = -1, len(s)
            k = 0
            
            if memo[i] == 1:
                curr_len = 2
                while i - k >= 0 and i + 1 + k < len(s):
                    left, right = i - k, i + 1 + k
                    if s[left] == s[right]:
                        k += 1
                        curr_len += 2
                    else:
                        break
            elif memo[i] == 2:
                curr_len = 3
                while i - 1 - k >= 0 and i + 1 + k < len(s):
                    left, right = i - 1 - k, i + 1 + k
                    if s[left] == s[right]:
                        k += 1
                        curr_len += 2
                    else:
                        break
            if curr_len > max_len:
                max_len = curr_len
                output = s[left:right + 1]
                
        return output