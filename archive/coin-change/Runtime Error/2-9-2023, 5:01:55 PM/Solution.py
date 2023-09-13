// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0.0] + [+math.inf for _ in range(amount)]
        for i in range(1, amount + 1):
            local_min = +math.inf
            for coin in coins:
                local_min = min(local_min, memo[i - coin] + 1)
            memo[i] = local_min
        return -1 if memo[amount] == +math.inf else int(memo[amount])