// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def backtrack(dice, rem):
            if dice == 0 and rem == 0:
                return 1
            if dice < 0 or rem < 0:
                return 0
            return sum(backtrack(dice - 1, rem - i) 
                for i in range(1, k + 1))
        return backtrack(n, target) % MOD