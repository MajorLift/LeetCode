// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        output: List[List[int]] = []
        def backtrack(tmp = [], start = 0):
            output.append(tmp)
            for i in range(start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(tmp + [nums[i]], i + 1)
        backtrack()
        return output