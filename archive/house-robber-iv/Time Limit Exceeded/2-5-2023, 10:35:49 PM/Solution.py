// https://leetcode.com/problems/house-robber-iv

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        @cache
        def dp(idx, take, val, cnt):
            if idx == len(nums) or cnt == k:
                return val if cnt == k else +math.inf
            if take:
                return dp(idx + 1, False, max(val, nums[idx]), cnt + 1)
            return min(dp(idx + 1, True, val, cnt), dp(idx + 1, False, val, cnt))
        
        return min(dp(0, True, -math.inf, 0), dp(0, False, -math.inf, 0))