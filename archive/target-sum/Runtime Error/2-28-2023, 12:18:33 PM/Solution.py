// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        memo = [([0] * (2 * total + 1)) for _ in range(n)]
        memo[0][total + nums[0]] = 1
        memo[0][total - nums[0]] += 1
        for i in range(1, n):
            for acc in range(-total, total + 1):
                if memo[i - 1][acc + total] > 0:
                    memo[i][acc + total + nums[i]] += memo[i - 1][acc + total]
                    memo[i][acc + total - nums[i]] += memo[i - 1][acc + total]
        return memo[n - 1][target + total]