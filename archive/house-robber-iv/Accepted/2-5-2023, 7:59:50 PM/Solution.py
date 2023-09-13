// https://leetcode.com/problems/house-robber-iv

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def robs_K_or_more(capability):
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
            x=True, 
            lo=min(nums), 
            key=lambda x: robs_K_or_more(x)
        )