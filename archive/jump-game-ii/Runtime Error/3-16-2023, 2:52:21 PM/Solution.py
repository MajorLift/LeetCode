// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n
        for i in range(n - 1):
            memo[i + 1] = max(j + nums[j] for j in range(memo[i] + 1))
            if memo[i + 1] >= n - 1:
                break
        idx = n - 1
        while memo[idx] == 0:
            idx -= 1
        return idx