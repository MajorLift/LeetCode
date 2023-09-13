// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_seq = []
        for num in nums:
            idx = bisect_left(max_seq, num)
            if idx == len(max_seq):
                max_seq.append(num)
            else:
                max_seq[idx] = num
        return len(max_seq)