// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for i in range(n):
            lmax, rmax = 0, 0
            for j in range(i, -1, -1):
                lmax = max(lmax, height[j])
            for j in range(i, n):
                rmax = max(rmax, height[j])
            ans += min(lmax, rmax) - height[i]
        return ans