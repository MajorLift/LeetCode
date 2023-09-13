// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced

class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        b_cnt = 0
        for char in s[1:]:
            if char == 'b':
                b_cnt += 1
            else:
                dp = min(b_cnt, dp + 1)
        return dp