// https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        @cache
        def dp(idx = 0, decoded = ""):
            nonlocal cnt
            if idx < n and s[idx] == "0":
                return 0
            if idx >= n - 1:
                return 1
            cnt += dp(idx + 1, decoded + chr(int(s[idx]) - 1 + ord("A")))
            cnt += dp(idx + 2, decoded + chr(int(s[idx:idx+2]) - 1 + ord("A"))) if 10 <= int(s[idx:idx + 2]) <= 26 else 0
            return cnt
        return dp()