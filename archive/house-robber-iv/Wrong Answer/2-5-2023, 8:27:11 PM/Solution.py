// https://leetcode.com/problems/house-robber-iv

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_valid(capability):
            cnt, skip = 0, False
            for num in nums:
                if skip:
                    skip = False
                    continue
                if num <= capability:
                    cnt += 1
                    skip = True
            return cnt >= k

        return bisect_left(
            a=range(max(nums) + 1), 
            lo=min(nums) + 1,
            key=lambda val: is_valid(val),
            x=True)