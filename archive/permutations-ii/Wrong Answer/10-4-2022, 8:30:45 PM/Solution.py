// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        nums = sorted(nums)
        def backtrack(tmp: List[int] = [], used: List[bool] = [False] * n) -> None:
            nonlocal output, nums
            if len(tmp) == len(nums):
                output.append(tmp)
                return
            for i in range(n):
                if not used[i] and (nums[i] != nums[i - 1] or used[i - 1]):
                    backtrack(tmp + [nums[i]], used[:i] + [True] + used[i+1:])
        backtrack()
        return output