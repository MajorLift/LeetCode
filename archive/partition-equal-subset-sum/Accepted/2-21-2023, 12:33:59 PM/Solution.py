// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2 > 0:
            return False
        target = total // 2
        memo = [True] + [False] * target
        for num in nums:
            for i in range(target, num - 1, -1):
                if memo[i - num]:
                    memo[i] = True
        return memo[-1]