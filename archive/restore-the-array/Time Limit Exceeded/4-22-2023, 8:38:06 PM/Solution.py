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
            for i in range(start + 1, n + 1):
                if int(s[start:i]) > k:
                    cnt -= 1
                    break
                cnt += dp(i)
            return cnt
        return dp(0) % MOD