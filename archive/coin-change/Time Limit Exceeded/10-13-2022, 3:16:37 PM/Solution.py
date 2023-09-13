// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        output = []
        def backtrack(tmp = [], remainder = amount):
            if remainder == 0:
                output.append(len(tmp))
            if remainder > 0:
                for coin in coins:
                    backtrack(tmp + [coin], remainder - coin)
        backtrack()
        return min(output) if len(output) > 0 else -1