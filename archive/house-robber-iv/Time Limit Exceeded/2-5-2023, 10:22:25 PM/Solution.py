// https://leetcode.com/problems/house-robber-iv

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        @cache
        def dp(idx, take, cnt, val):
            if idx == len(nums) or cnt == k:
                return val if cnt == k else +math.inf
            if take:
                return dp(idx + 1, False, cnt + 1, max(val, nums[idx]))
            else:
                return min(dp(idx + 1, True, cnt, val), dp(idx + 1, False, cnt, val))
        return min(dp(0, True, 0, -math.inf), dp(0, False, 0, -math.inf))