// https://leetcode.com/problems/student-attendance-record-ii

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def dp(k, absent):
            if k < 3:
                if absent == 1:
                    return [1, 2, 4][k]
                if absent == 0:
                    return [1, 3, 8][k]
            if absent == 1:
                return (dp(k - 1, 1) + dp(k - 2, 1) + dp(k - 3, 1)) % MOD
            if absent == 0:
                return (dp(k - 1, 0) + dp(k - 2, 0) + dp(k - 3, 0) + dp(k, 1)) % MOD
        
        return dp(n, 0) % MOD