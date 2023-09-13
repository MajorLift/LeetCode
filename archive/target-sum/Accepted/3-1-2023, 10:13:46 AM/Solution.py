// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n, total = len(nums), sum(nums)
        memo = defaultdict(int)
        memo[(0, +nums[0])] = 1
        memo[(0, -nums[0])] += 1
        for i in range(1, n):
            for acc in range(-total, total + 1):
                if memo[(i - 1, acc)] > 0:
                    memo[(i, acc + nums[i])] += memo[(i - 1, acc)]
                    memo[(i, acc - nums[i])] += memo[(i - 1, acc)]
        return memo[(n - 1, target)] if abs(target) <= total else 0