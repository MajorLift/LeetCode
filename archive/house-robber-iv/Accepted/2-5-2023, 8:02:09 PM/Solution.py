// https://leetcode.com/problems/house-robber-iv

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def robs_K_or_more(capability):
            cnt, skips = 0, set()
            for i in (x for x in range(len(nums)) if x not in skips):
                if nums[i] <= capability:
                    cnt += 1
                    skips.add(i + 1)
            return cnt >= k

        return bisect_left(
            a=range(max(nums) + 1), 
            x=True, 
            lo=min(nums), 
            key=lambda x: robs_K_or_more(x)
        )