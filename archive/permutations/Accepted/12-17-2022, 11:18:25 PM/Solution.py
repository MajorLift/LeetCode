// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output: List[List[int]] = []
        def backtrack(tmp: List[int] = [], used: List[bool] = [False] * n):
            if len(tmp) == len(nums):
                output.append(tmp)
            for i in range(n):
                if not used[i]:
                    backtrack(tmp + [nums[i]], used[:i] + [True] + used[i+1:])
        backtrack()
        return output