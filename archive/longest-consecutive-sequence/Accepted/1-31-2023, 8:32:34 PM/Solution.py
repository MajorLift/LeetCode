// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans = 0
        for num in hashset:
            if num - 1 not in hashset:
                curr = num
                local = 0
                while curr in hashset:
                    curr += 1
                    local += 1
                ans = max(ans, local)
        return ans
        