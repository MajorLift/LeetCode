// https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)

        max_idx = 0, 0
        for i in range(n):
            max_idx = max(max_idx, expand(i, i + 1), expand(i - 1, i + 1), key=lambda x: x[1] - x[0])
        l, r = max_idx
        return s[l:r + 1]