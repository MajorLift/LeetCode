// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [nums[0]]
        for num in nums[1:]:
            if num > subseq[-1]:
                subseq.append(num)
            else:
                subseq[bisect_left(subseq, num)] = num
        return len(subseq)