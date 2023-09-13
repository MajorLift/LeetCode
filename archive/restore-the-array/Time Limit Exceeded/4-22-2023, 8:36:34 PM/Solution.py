// https://leetcode.com/problems/restore-the-array

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        @cache
        def dp(start):
            if start == n:
                return 0
            if s[start] == "0":
                return 0
            cnt = 1
            for i in range(start, n):
                if int(s[start:i + 1]) > k:
                    cnt -= 1
                    break
                cnt += dp(i + 1)
            return cnt
        return dp(0) % MOD