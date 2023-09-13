// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [0] * n
        for i in range(1, n):
            memo[i] = max(j + nums[j] for j in range(memo[i - 1] + 1))
            if memo[i] >= n - 1:
                break
                
        while memo and memo[-1] == 0:
            memo.pop()
        return max(len(memo) - 1, 0)