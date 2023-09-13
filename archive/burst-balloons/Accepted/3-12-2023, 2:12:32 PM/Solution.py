// https://leetcode.com/problems/burst-balloons

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(l, r):
            if l > r:
                return 0
            return max(dp(l, i - 1) 
                    + (nums[l - 1] if l > 0 else 1) 
                        * nums[i] 
                        * (nums[r + 1] if r < n - 1 else 1)
                    + dp(i + 1, r)
                for i in range(l, r + 1))
        return dp(0, n - 1)