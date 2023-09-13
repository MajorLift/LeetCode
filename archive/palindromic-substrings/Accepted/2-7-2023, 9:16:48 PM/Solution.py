// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            ans = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            return ans

        ans = 0
        for i in range(len(s)):
            ans += expand(i, i + 1) + expand(i, i)
        return ans