// https://leetcode.com/problems/partition-equal-subset-sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if total % 2 > 0:
            return False
        target = total // 2
        memo = [True] + [False] * target
        for i in range(target, 0, -1):
            for num in nums:
                if i < num: continue
                memo[num] = memo[num] or memo[i - num]
        return memo[-1]