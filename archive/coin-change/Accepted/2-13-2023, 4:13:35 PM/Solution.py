// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0.0] + [+math.inf] * amount
        for i in range(1, amount + 1):
            memo[i] = 1 + min(memo[i - coin] if i - coin >= 0 else +math.inf for coin in coins)
        return int(memo[-1]) if memo[-1] < +math.inf else -1