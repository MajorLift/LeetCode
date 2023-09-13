// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        def backtrack(tmp: List[int] = []):
            nonlocal output, nums
            if len(tmp) == len(nums):
                output.append(tmp)
            for i in range(n):
                if nums[i] not in tmp:
                    backtrack(tmp + [nums[i]])
        backtrack()
        return output
            