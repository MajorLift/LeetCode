// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def backtrack(cnt, remaining):
            if cnt == n:
                return int(remaining == 0)
            return sum(backtrack(cnt + 1, remaining - i) 
                        for i in range(1, k + 1)) % MOD
        return backtrack(0, target) % MOD