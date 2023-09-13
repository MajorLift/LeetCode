// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        prev = [0] * (2 * total + 1)
        prev[total + nums[0]] = 1
        prev[total - nums[0]] += 1
        for i in range(1, n):
            curr = [0] * (2 * total + 1)
            for acc in range(-total, total + 1):
                if prev[acc + total] > 0:
                    curr[acc + total + nums[i]] += prev[acc + total]
                    curr[acc + total - nums[i]] += prev[acc + total]
            prev = curr
        return prev[target + total]