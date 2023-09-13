// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        cnt = 0
        @cache
        def dp(idx):
            nonlocal cnt
            if idx >= len(s):
                return 1
            if s[idx] == "0":
                return 0
            cnt += dp(idx + 1) + (dp(idx + 2) if 10 <= int(s[idx:idx + 2]) <= 26 else 0)
            return cnt
        return dp(0)